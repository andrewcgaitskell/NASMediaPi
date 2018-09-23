import os

path = '/mnt/PIHDD'

dir_entries = os.scandir(path)

for entry in dir_entries:
    info = entry.stat()
    print(info)
