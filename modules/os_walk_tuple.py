'''Dictionary for dir:file'''

import os

def run(**args):
    
    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
       dname = dirName
       fname = fileList
       lists = dname, fname
    return str(lists)
    
    
   

    
        

    
    
   
    
