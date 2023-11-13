import os

DIRECTORY = '../DATA'

for entry_name in os.listdir(DIRECTORY):
    file_path = os.path.join(DIRECTORY, entry_name)
    file_size = os.path.getsize(file_path)
    print(f"{entry_name:50s} {file_size:10d}")

