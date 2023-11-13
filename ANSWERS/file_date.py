import sys
import os
from datetime import datetime

for filename in sys.argv[1:]:
    mtime = os.path.getmtime(filename)
    file_date = datetime.fromtimestamp(mtime)
    fmt_date = file_date.strftime('%b %d, %Y')
    print(f"{filename:15s} {fmt_date}")
