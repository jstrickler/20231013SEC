import os
from datetime import datetime


def format_time(time_stamp):
    """convert time stamp to YYYY-MM-DD HH:MM string"""
    date_time = datetime.fromtimestamp(time_stamp)  # convert epoch time to Python datetime
    time_string = date_time.strftime('%Y-%m-%d %H:%M')  # format datetime object

    return time_string


filenames = (  # files to test
    '../DATA/alice.txt',
    '../ANSWERS/sieve.py',
    'file_attrib.py',
)

for filename in filenames:
    size = os.path.getsize(filename)  # get size of file
    mtime_ts = os.path.getmtime(filename)  # get file timestamp (last time file was modified)
    mtime = format_time(mtime_ts)

    atime_ts = os.path.getatime(filename)  # get file timestamp (last time file was read)
    atime = format_time(atime_ts)

    print(f'{filename:20s} {size:8d}  {mtime}  {atime}')
