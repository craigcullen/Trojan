import os
import sys

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    
    return files
    return os.path.dirname(sys.argv[0])
