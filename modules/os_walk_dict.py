'''Dictionary for dir:file'''

import os

rootDir = "/home/craig/Documents"

def run(**args):

    print "[*] In os_walk_dict module"

    for dirName, subdirList, fileList in os.walk(rootDir):
        files = {dirName : [fname for fname in fileList]}
        return str(files)
    
