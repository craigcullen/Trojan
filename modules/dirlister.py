import os
import sys

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return str(files)
    return str(os.path.dirname(sys.argv[0]))
