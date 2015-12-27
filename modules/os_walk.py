'''Simple os walk script'''

import os

def run1(**args):
    print "[*] In os_walk module_1"

    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        return dirName

def run2(**arges):
    print "[*] In os_walk module_2"
    
    rootDir = "/home/craig/Documents"

    for dirName, subdirlist, fileList in os.walk(rootDir):
        for fname in fileList:
            return fname
        
