'''Simple os walk script'''

import os

rootDir = "/home/craig/Documents"

for dirName, subdirList, fileList in os.walk(rootDir):
    return "Found directory: %s" % dirName
    for fname in fileList:
        return "\t%s" % fname
