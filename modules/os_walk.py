'''Simple os walk script'''

import os

rootDir = "/home/craig/Documents"

def run(**args):
    print "[*] In os_walk module"

    dir_name = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        dir_name.append(dirName)
        
    return str(dir_name)
    
