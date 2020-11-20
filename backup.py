import os
import shutil
name=input('enter source folder name' )
destination=input('enter destination folder name')
name=name+'/'
destinaton=destination+'/'
listoffiles=os.listdir(name)
for file in listoffiles:
    shutil.copy((name+file),destinaton)