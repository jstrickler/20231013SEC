import shutil
import os

folder = '../DATA'
archive_name = "datafiles"

for archive_type in 'zip', 'tar', 'gztar', 'bztar':
    shutil.make_archive(archive_name, archive_type, folder)



