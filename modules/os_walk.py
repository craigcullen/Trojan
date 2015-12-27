'''Simple os walk script'''

import os

def run(**args):
    print "[*] In os_walk module"

    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            return fname


        
