import os
import shutil

files_to_copy = []

for file_name in os.listdir('../DATA'):
    if file_name.startswith('p'):
        files_to_copy.append(file_name)

for file_to_copy in files_to_copy:
    file_path_to_copy = os.path.join('../DATA', file_to_copy)
    shutil.copy(file_path_to_copy, '../TEMP')
