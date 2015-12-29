'''Dictionary for dir:file'''

import os

def run(**args):
    print "[*] In os_walk_tuple module"
    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        files = ([dirName], [fname for fname in fileList])
       
    	return files[0], files[1]
    
   

    
        

    
    
   
    
