import pathlib
import shutil
from operator import itemgetter
import hashlib
import os

INVALID_VALUE = -1
NO_ERROR_VALUE = 0

__name__ = "my_utils"
__version__ = 1.0


def get_file_name_from_path(fullpathtofile):
    """ return filename from full path file name """
    path = pathlib.Path(fullpathtofile)
    return str(path.name)


#def get_folder_name_from_path(strfullpathtofile):
#    """ return folder name from full path file name """
#    mypath = pathlib.Path().absolute()
#    return str(mypath)


def get_folder_file_list(str_full_folder_path_name):
    """Return list of files in folder str_full_folder_path_name.
    Each list item contains a tuple of two elements (filename_without_path, file_size_in_bytes).
    Returned list sorted by file_size ascending """
    flist = None

    lpath = pathlib.Path(str_full_folder_path_name)
    if not lpath.is_dir():
        return flist # return None if str_full_folder_path_name not folder

    flist = list()
    # enumerating files ONLY!!!
    for child in lpath.iterdir():
        if child.is_file():
            file = pathlib.Path(child.absolute())
            file_size = file.stat().st_size
            item_tuple = (child.name, file_size)
            flist.append(item_tuple)

    return sorted(flist, key=itemgetter(1))


def get_hash_file(path: str, algorithm="md5", bufsize=4096):
    """return hash of file"""
    h = hashlib.new(algorithm)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(bufsize), b""):
            h.update(chunk)

    return h.digest()


def is_folder_exist(full_folder_path):
    """check folder for exist and is folder
    return value is Boolean!"""
    folder = pathlib.Path(full_folder_path)
    return folder.is_dir() and folder.exists()


def get_full_file_name(str_folder_owner, str_file_name):
    """returns the full file name adding the folder name and file name"""
    return str_folder_owner + os.path.sep + str_file_name


def delete_duplicate_file(folder_full_path, storage_folder=None):
    """move/delete duplicate files of the same size and context in specified folder (folder_full_path).

    folder_full_path - folder where duplicates are searched.
    storage_folder - optional - folder for storage duplicate files
    If the storage_folder is not specified, then duplicate files will be deleted!

    in case of error returns a negative value.
    if successful, returns the number of found duplicate files subjected to move / delete
    """
    ret_val = INVALID_VALUE

    if not is_folder_exist(folder_full_path):
        return ret_val

    # START
    if storage_folder is not None and not is_folder_exist(storage_folder):
        return ret_val

    file_list = get_folder_file_list(folder_full_path)

    if 0 == len(file_list): # zero files for compare. exit
        return NO_ERROR_VALUE

    tpl_first = None

    INDEX_FILE_NAME, INDEX_FILE_SIZE = range(2)

    ret_val = NO_ERROR_VALUE

    for item in file_list:
        if tpl_first is None:
            tpl_first = item
            continue
        if item[INDEX_FILE_SIZE] == tpl_first[INDEX_FILE_SIZE]:
            fname = get_full_file_name(folder_full_path, item[INDEX_FILE_NAME])
            hash = get_hash_file(fname)
            hash1 = get_hash_file(
                    get_full_file_name(folder_full_path, tpl_first[INDEX_FILE_NAME]))
            if hash == hash1:
                if storage_folder is None:
                    f = pathlib.Path(fname)
                    f.unlink() # delete file
                    ret_val+=1
                    #print("File {0} deleted.".format(fname))
                else:
                    dst = get_full_file_name(storage_folder , item[INDEX_FILE_NAME])
                    # move duplicate file to storage folder
                    shutil.move(fname, dst, copy_function = shutil.copy)
                    ret_val += 1
                    #print("File {0} moved to {1}".format(fname, dst))
        else: # file size not equals
            tpl_first = item
            continue

    return ret_val
