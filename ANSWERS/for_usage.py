import os
import re

rx_forloop = re.compile(r'\bfor\b')

for_count = 0

for curr_dir, dir_list, file_list in os.walk('..'):
    for file_name in file_list:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            with open(file_path) as FP:
                for line in FP:
                    if rx_forloop.search(line):
                        for_count += 1

print("for is used {} times".format(for_count))
