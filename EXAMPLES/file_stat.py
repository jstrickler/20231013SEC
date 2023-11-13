import os

info = os.stat('../DATA/parrot.txt')  # get stat data for file
print(info)  # print all data, which is a named tuple

print('size is', info[6])  # get the file size by numeric index
print('size is', info.st_size)  # get the file size by field name
