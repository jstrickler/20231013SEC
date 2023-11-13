
import sys
import os

if len(sys.argv) < 2:
    start_dir = "."
else:
    start_dir = sys.argv[1]

for base_name in os.listdir(start_dir):  # os.listdir() lists the contents of a directory
    file_name = os.path.join(start_dir, base_name)
    if os.access(file_name, os.W_OK):  # os.access() returns True if file has specified permissions (can be os.W_OK, os.R_OK, or os.X_OK, combined with | (OR))
        print(file_name, "is writable")
