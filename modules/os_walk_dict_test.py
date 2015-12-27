'''Dictionary for dir:file'''

import os

def run(**args):

    print "[*] In os_walk_dict_test module"

    rootDir = "/home/craig/Documents"
    all_files = {}

    for dirName, subdirList, fileList in os.walk(rootDir):
        files = {dirName : [fname for fname in fileList]}    
        for fil in files:
            all_files.update(fil)
            return all_files

        
