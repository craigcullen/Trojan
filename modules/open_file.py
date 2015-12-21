import os

def run(**args):
    print "[*] In file_id module."
    with open ('/home/craig/Documents/Python/get_ip.py', 'rb') as fin:
        file = fin.read()
    return file
