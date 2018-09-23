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
        fullpathtofile = os.path.join(directory,i)
        # print(b)
        fullfilename = i
        if fullfilename[0] != "." :
            foldersaslist = fullpathtofile.split(".")
            foldercount = len(foldersaslist)
            containingfolder = foldersaslist[foldercount-1]
            justfilenamesplit = fullfilename.split(".")
            fileextension = justfilenamesplit[1]
            filename = justfilenamesplit[0]
            lastmodifieddate = time.ctime(a.st_atime)
            createddate = time.ctime(a.st_ctime)
            file_list.append([containingfolder,filename,fileextension,lastmodifieddate,createddate]) #[file,most_recent_access,created]
    return file_list

a = get_information("/mnt/PIHDD/data")

print(a)
