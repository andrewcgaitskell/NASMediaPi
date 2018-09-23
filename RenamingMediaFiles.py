import os

with os.scandir() as dir_entries:
    for entry in dir_entries:
        info = entry.stat()
        print(info)
