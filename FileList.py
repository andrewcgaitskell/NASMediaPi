import os,time
import psycopg2
import config

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
        fullpathtooriginalfile = os.path.join(directory,i)
        # print(b)
        fullfilename = i
        if fullfilename[0] != "." :
            foldersaslist = fullpathtooriginalfile.split("/")
            foldercount = len(foldersaslist)
            containingfolder = foldersaslist[foldercount-2]
            justfilenamesplit = fullfilename.split(".")
            originalfileextension = justfilenamesplit[1]
            originalfilename = justfilenamesplit[0]
            # lastmodifieddate = time.ctime(a.st_atime)
            # createddate = time.ctime(a.st_ctime)
            lastmodifieddatetuple = time.gmtime(a.st_atime)
            # lastmodifieddateiso = time.strftime("%Y-%m-%dT%H:%M:%S", lastmodifieddatetuple)
            lastmodifieddateid = time.strftime("%Y%m%d%H%M%S", lastmodifieddatetuple)
            createddatetuple = time.gmtime(a.st_ctime)
            # createddateiso = time.strftime("%Y-%m-%dT%H:%M:%S", createddatetuple)
            createddateid = time.strftime("%Y%m%dT%H%M%S", createddatetuple)
            createdyear = createddateid[0:4]
            createdmonth = createddateid[0:6]
            newfilename = lastmodifieddateid + "." + originalfileextension
            file_list.append([fullpathtooriginalfile,containingfolder,originalfilename,originalfileextension,lastmodifieddateid,createddateid,createdyear,createdmonth,newfilename])
    return file_list

a = get_information("/mnt/PIHDD/data")

print(a)


# conn = psycopg2.connect('dbname=files')
# cur = conn.cursor()

conn = None
commands = ('DROP TABLE IF EXISTS data;');

try:
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()

commands = (
    '''CREATE TABLE data (
    fullpathtooriginalfile VARCHAR(255),
    containingfolder VARCHAR(255),
    originalfilename VARCHAR(255),
    originalfileextension VARCHAR(255),
    lastmodifieddateid VARCHAR(255),
    createddateid VARCHAR(255),
    createdyear VARCHAR(255),
    createdmonth VARCHAR(255),
    newfilename VARCHAR(255)'''
    );
    
try:
    # read the connection parameters
    params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    # create table one by one
    for command in commands:
        cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


