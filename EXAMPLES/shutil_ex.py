import shutil
import os

shutil.copy('../DATA/alice.txt', 'betsy.txt') # copy file

print("betsy.txt exists:", os.path.exists('betsy.txt'))

shutil.move('betsy.txt', 'fred.txt') # rename file
print("betsy.txt exists:", os.path.exists('betsy.txt'))
print("fred.txt exists:", os.path.exists('fred.txt'))

new_folder = 'remove_me'

os.mkdir(new_folder) # create new folder
shutil.move('fred.txt', new_folder)

shutil.rmtree(new_folder) # recursively remove folder

print(f"{new_folder} exists:", os.path.exists(new_folder))
