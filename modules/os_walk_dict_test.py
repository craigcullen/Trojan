'''Dictionary for dir:file'''

import os

def run(**args):

    print "[*] In os_walk_dict_test module"

    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        files = {dname for dname in dirName : [fname for fname in fileList]}
        return str(files)
    
