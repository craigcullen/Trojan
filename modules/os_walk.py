'''Simple os walk script'''

import os

rootDir = "/home/craig/Documents"

def run(**args):

    dir_name = []
    #file_name = ""
    for dirName, subdirList, fileList in os.walk(rootDir):
        dir_name.append(dirName)
        #for fname in fileList:
            #file_name += fname

    return str(dir_name)
    
