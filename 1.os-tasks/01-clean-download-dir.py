import os
import datetime as dt
import shutil
from pathlib import Path

downdir='/Users/vikas/Downloads/'
tempdir='/Users/vikas/temp'
daysToMoveTempDir=60
daysToDeleteFromTemp=90


currentdate = dt.datetime.now()

# delete from temp dir 
os.chdir(tempdir)
dirs = os.listdir()
print('####removing from temp directory')
for dir in dirs:
    filechangetime = dt.datetime.fromtimestamp(os.stat(dir).st_mtime)
    dateDiff = currentdate - filechangetime
    
    if dateDiff.days > daysToDeleteFromTemp:
        print(dir, ", days diff: ", dateDiff.days)
        print("is file: ",Path(dir).is_file())
        
        if Path(dir).is_file():
            print(os.remove(dir))
        else:
            shutil.rmtree(dir)

print('####cleaning from download directory')
os.chdir(downdir)
dirs = os.listdir()
# move to temp dir 
for dir in dirs:
    filechangetime = dt.datetime.fromtimestamp(os.stat(dir).st_atime)
    dateDiff = currentdate - filechangetime
    if dateDiff.days > daysToMoveTempDir:
        shutil.move(dir, tempdir, copy_function='copy2')
       

print('finished')

