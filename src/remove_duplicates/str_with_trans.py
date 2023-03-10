"""строки, c переводом"""
import os
import locale
import pathlib
import remove_duplicates.internationalization as my_int

# чтобы активировать пользовательскую locale! Для форматирования даты и времени!
# locale.setlocale(locale.LC_ALL, '')
# текущий язык локали
curr_lang = locale.getdefaultlocale()[0][:2].upper()
# полный путь к файлу
src_folder = pathlib.Path(__file__).parent
# чтение интернационализированных строк
_I = my_int.CSVProvider(f"{src_folder}{os.path.sep}translated.csv", "strID", curr_lang)

# переводимые на другие языки строки

strAccessError = "Access is denied! Folder:"
strProcessInfo = "Folder {start} processed. Found {retval} copies!"

strDescription = """Utility to recursive search and move/delete duplicate files 
                    of the same size and context in specified folder."""
strEpilog = """If the storage folder is not specified, 
                then duplicate files will be deleted!
                If the number of command line parameters is zero, 
                then the search folder = current folder."""

strRecursiveSearchBegin = "The folder with which the recursive search begins."
strFolderForStor = "Folder for storing duplicate files."
strLogFileName = "Log file name."
strFileNamePattern = "File name pattern. Only files matching the pattern are processed! " \
                     "Provides support for Unix shell-style wildcards."
strNotRecursively = "If this parameter is set, then recursive search is disabled!"
strInvalidSearchFolder = "Invalid path to search folder: {search_folder}. Exit!"
strInvalidStorageFolder = "Invalid path to storage folder: {stor_folder}. Exit!"

strSearchForDupFilesInFolder = "Search for duplicate files in the folder: {folder_name}"
strPatternFileName = "Pattern file name: {pattern}"
strLogFileName_1 = "Log file name: {log}"
strStorFolder = "Storage folder: {storage}"
strRecursiveSearchDisabled = "Recursive search disabled!"
strActionDel = "deleted"
strActionMov = "moved"
strTotalFound = "Total found {total} copies of files."
strLastInfo = "{cnt} copies of files have been {action}."
