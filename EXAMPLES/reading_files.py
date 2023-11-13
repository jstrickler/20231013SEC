
FILE_NAME = '../DATA/mary.txt'

mary_in = open(FILE_NAME)  # open file for reading
# read file...
mary_in.close()  # close file (easy to forget to do this!)

with open(FILE_NAME) as mary_in:  # open file for reading
    for raw_line in mary_in:  # iterate over lines in file (line retains \n)
        line = raw_line.rstrip()  # rstrip('') removes whitespace (including \n or \r ) from end of string
        print(line)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("NORMAL:")
    print(contents)
    print("=" * 20)
    print("RAW:")
    print(repr(contents))  # print string in "raw" mode
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_with_nl = mary_in.readlines()  # readlines() reads all lines into an array
    print(lines_with_nl)
print('-' * 60)

with open(FILE_NAME) as mary_in:
    lines_without_nl = mary_in.read().splitlines()  # splitlines() splits string on ' ' into lines
    print(lines_without_nl)
