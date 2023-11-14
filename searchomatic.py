from glob import glob
import os
import som_config as config

#  create list of files from wildcards
#  for each file
#     create path using folder
#     open flie
#        for line in file
#            for search_term in term list
#               if search_term in line, write file name, line #, line to results file

all_files = []
os.chdir(config.search_folder)
for file_arg in config.search_files:
    all_files.extend(glob(file_arg))

with open('results.txt', 'w') as results_out:
    for file_name in all_files:
        with open(file_name) as file_in:
            for line_number, raw_line in enumerate(file_in, 1):
                for term in config.search_terms:
                    if term.lower() in raw_line.lower():
                        output = f"{file_name}:{line_number}:{raw_line}"
                        results_out.write(output)
