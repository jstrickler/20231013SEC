
import os

for path in ('c:/windows', '/etc', '../DATA', '/wombat', '/tmp', 'RESULTS', 'C:/temp'):  # loop through some files and folders that may or may not exist
    print(path, end=' ')  # print path to be checked, but stay on same line (output space instead of newline)
    if os.path.exists(path):  # check for existence
        print('exists')
    else:
        print('does not exist')
