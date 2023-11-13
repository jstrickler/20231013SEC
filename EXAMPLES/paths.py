import sys
import os.path

unix_p1 = "bin/spam.txt"  # Unix relative path
unix_p2 = "/usr/local/bin/ham"  # Unix absolute path

win_p1 = r"spam\ham.doc"  # Windows relative path
win_p2 = r"\\spam\ham\eggs\toast\jam.doc"  # Windows UNC path

if sys.platform == 'win32':  # Are we on Windows?
    print("win_p1:", win_p1)
    print("win_p2:", win_p2)
    print("dirname(win_p1):", os.path.dirname(win_p1))  # Just the folder name
    print("dirname(win_p2):", os.path.dirname(win_p2))
    print("basename(win_p1):", os.path.basename(win_p1))  # Just the file (or folder) name
    print("basename(win_p2):", os.path.basename(win_p2))
    print("isabs(win_p1):", os.path.isabs(win_p1))  # Is it an absolute path?
    print("isabs(win_p2):", os.path.isabs(win_p2))
else:  # Mac/Linux
    print("unix_p1:", unix_p1)
    print("unix_p2:", unix_p2)
    print("dirname(unix_p1):", os.path.dirname(unix_p1))  # Just the folder name
    print("dirname(unix_p2):", os.path.dirname(unix_p2))
    print("basename(unix_p1):", os.path.basename(unix_p1))  # Just the file (or folder) name
    print("basename(unix_p2):", os.path.basename(unix_p2))
    print("isabs(unix_p1):", os.path.isabs(unix_p1))  # Is it an absolute path?
    print("isabs(unix_p2):", os.path.isabs(unix_p2))
    print(f"os.path.expanduser('~'): {os.path.expanduser('~')}")
    print(f"os.path.expanduser('~root'): {os.path.expanduser('~root')}")
    