import os,time

def files(path):  
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
            
for file in files("."):  
    print (file);
    
def get_information(directory):
    file_list = []
    for i in os.listdir(directory):
        a = os.stat(os.path.join(directory,i))
        fullfilename = i
        justfilenamesplit = fullfilename.split(".")
        lastmodifieddate = time.ctime(a.st_atime)
        createddate = time.ctime(a.st_ctime)
        file_list.append([justfilenamesplit,lastmodifieddate,createddate]) #[file,most_recent_access,created]
    return file_list

a = get_information("/mnt/PIHDD/data")

print(a)
