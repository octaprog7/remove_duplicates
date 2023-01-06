Utility to recursive search and move/delete duplicate files of the same size and context in specified folder.

If the storage folder (recycle_bin) is not specified, then duplicate files will be deleted!
If the number of command line parameters is zero, then the search folder = current folder.

### Command line parameters
    --start_folder (first parameter): the folder with which the recursive search begins
    --recycle_bin (second parameter): optional folder for storing duplicate files (move file).
    --log_file: log file.
    --fn_pattern: File name pattern. Only files matching the pattern are processed!
                   Provides support for Unix shell-style wildcards. Default value is "*.*"

### Call example
    remove_duplicates --start_folder=E:\YoutubeChannelsCopy --recycle_bin=E:\reserved --log_file=E:\reserved\logfile.txt --fn_pattern="*.png" 
## Work log
![alt text](https://github.com/octaprog7/remove_duplicates/blob/master/warn_del.png)
## PyPi
https://pypi.org/project/remove-duplicates/