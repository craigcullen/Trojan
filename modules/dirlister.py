import os
import sys

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    path = os.getcwd()
    
    return str(files)
    return str(path)
    
