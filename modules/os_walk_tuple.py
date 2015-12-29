'''Dictionary for dir:file'''

import os

def run(**args):
    print "[*] In os_walk_tuple module"
    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        filedict = {dirName: [fname for fname in fileList]}
       
    	return str(filedict)
    
   

    
        

    
    
   
    
