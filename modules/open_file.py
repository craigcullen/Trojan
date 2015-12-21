import os

def run(**args):
    print "[*] In file_id module."
    with open ('get_ip.py', 'rb') as fin:
        file = fin.read()
    return file
