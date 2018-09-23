import os,time

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def get_information(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        file_list.append([i,time.ctime(a.st_atime),time.ctime(a.st_ctime)]) #[file,most_recent_access,created]
    return file_list

for file in files("."):  
    print (file);

print get_information("/mnt/PIHDD/data")
