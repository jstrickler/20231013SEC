
# count number of files and dirs in  a directory tree
# note "files" includes devices, symbolic links, and pipes
import os
import sys

if sys.platform == 'win32':  # check platform
    target = 'C:/Users'
else:
    target = '/etc'

total_files = 0  # initialize counters
total_dirs = 0

for currdir, subdirs, files in os.walk(target):  # visit target folder and each subfolder; os.walk() returns 3-tuple at each folder
    total_dirs += 1  # increment number of directories seen
    total_files += len(files)  # add the number of files in this dir

print(f"{target} contains {total_dirs} dirs and {total_files} files")  # output results
