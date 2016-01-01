'''Simple os walk script'''

import os

rootDir = "/home/craig/Documents"

def run(**args):
    print "[*] In os_walk_files module"

    file_list = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        file_list.append(fileList)
        
    return str(file_list)
    
