import os

def run(**args):
    print "[*] In file_id module."
    with open ('environment.py', 'rb') as fin:
        file = fin.ready()
    return file
