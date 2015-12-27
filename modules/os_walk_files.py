'''Simple os walk script'''

import os

rootDir = "/home/craig/Documents"

def run(**args):
    print "[*] In os_walk_files module"

    file_name = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            file_name.append(fname)
        
    return str(file_name)
   
