import os

DIRECTORY = '../DATA'

for entry in os.scandir(DIRECTORY):
    stat_info = entry.stat()
    print(f"{entry.name:50s} {stat_info.st_size:10d} {entry.is_file()!s:5s} {entry.is_dir()!s:5s} {stat_info.st_mode:06o}")
