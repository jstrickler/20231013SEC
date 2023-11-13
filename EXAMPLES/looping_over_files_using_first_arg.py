import sys

first_arg = sys.argv.pop(1)

print(f"first arg is '{first_arg}'")
for file_path in sys.argv[1:]:  # skip script name
    print(f"Processing {file_path}")
    with open(file_path) as file_in:
        pass   #  read each file here

