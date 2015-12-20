import os

def run(**args):
    print "[*] In file_id module."
    with open ('/root/trojan/modules/environment.py', 'rb') as fin:
        file = fin.read()
    return file
