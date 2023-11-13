"""
    find files whose size is greater than or equal to specified number of bytes
"""
import sys
import os

MINIMUM_SIZE = 1000

if len(sys.argv) < 2: # make sure there is at least one command line argument
    print('Syntax: walk2.py START-DIR')
    sys.exit(1)

for currdir, subdirs, files in os.walk(sys.argv[1]):
    for file in files: # in each folder, iterate over files
        fullpath = os.path.join(currdir, file) # get full path to file
        if os.path.isfile(fullpath): # make sure it's a file (not a link or device, etc.)
            fsize = os.path.getsize(fullpath) # get file size
            if fsize >= MINIMUM_SIZE: # check size to see if it's at least MINIMUM_SIZE
                print(f"{fsize:8d} {fullpath:40s}")
