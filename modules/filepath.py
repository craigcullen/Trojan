import os
import sys

def run(**args):
    print "[*] In filepath module"
    path = os.path.dirname(sys.argv[0])
    return str(path)
