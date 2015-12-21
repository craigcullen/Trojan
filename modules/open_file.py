import os

def run(**args):
    print "[*] In file_id module."
    with open ('input_file_path', 'rb') as fin:
        file = fin.read()
    return file
