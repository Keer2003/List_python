import os
rootDir="c:\\python_learning"
fileToSearch="for.py"

for relpath,dirs,files in os.walk(rootDir):
    if(fileToSearch in files):
        fullpath=os.path.join(rootDir,relpath,fileToSearch)
        print(fullpath)
