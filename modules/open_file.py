import os

def run(**args):
    print "[*] In open_file module."
    with open ('get_ip.py', 'rb') as fin:
        return fin.read()
