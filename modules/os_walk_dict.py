'''Dictionary for dir:file'''

import os

rootDir = "/home/craig/Documents"

for dirName, subdirList, fileList in os.walk(rootDir):
    files = {dirName : [fname for fname in fileList]}
    return str(files)
    
