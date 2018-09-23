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
            foldersaslist = fullpathtofile.split("/")
            foldercount = len(foldersaslist)
            containingfolder = foldersaslist[foldercount-2]
            justfilenamesplit = fullfilename.split(".")
            fileextension = justfilenamesplit[1]
            filename = justfilenamesplit[0]
            # lastmodifieddate = time.ctime(a.st_atime)
            # createddate = time.ctime(a.st_ctime)
            lastmodifieddatetuple = time.gmtime(a.st_atime)
            # lastmodifieddateiso = time.strftime("%Y-%m-%dT%H:%M:%S", lastmodifieddatetuple)
            lastmodifieddateid = time.strftime("%Y%m%d%H%M%S", lastmodifieddatetuple)
            createddatetuple = time.gmtime(a.st_ctime)
            # createddateiso = time.strftime("%Y-%m-%dT%H:%M:%S", createddatetuple)
            createddateid = time.strftime("%Y%m%dT%H%M%S", createddatetuple)
            createdyear = createddateid[0:3]
            createdmonth = createddateid[4:5]
            file_list.append([fullpathtofile,containingfolder,filename,fileextension,lastmodifieddateid,createddateid,createdyear,createdmonth])
    return file_list

a = get_information("/mnt/PIHDD/data")

print(a)
