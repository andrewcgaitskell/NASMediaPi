import os

path = '/mnt/PIHDD'

with os.scandir(path) as dir_entries:
    for entry in dir_entries:
        info = entry.stat()
        print(info)
