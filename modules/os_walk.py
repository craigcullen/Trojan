'''Simple os walk script'''

import os

def run(**args):
    print "[*] In os_walk module"

    rootDir = "/home/craig/Documents"

    for dirName, subdirList, fileList in os.walk(rootDir):
        print "Found directory: %s" % dirName
        for fname in fileList:
            print "\t%s" % fname
