Utility to recursive search and move/delete duplicate files of the same size and context in specified folder.

If the storage folder (recycle_bin) is not specified, then duplicate files will be deleted!
If the number of command line parameters is zero, then the search folder = current folder.

### Command line parameters
    --start_folder (first parameter). The folder with which the recursive search begins
    --recycle_bin (second parameter). Optional folder for storing duplicate files (move file).
    --log_file. Log file.

### Call example
    remove_duplicates --start_folder=E:\YoutubeChannelsCopy --recycle_bin=E:\reserved --log_file=E:\reserved\logfile.txt