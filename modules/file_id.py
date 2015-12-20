import os

file_id = []

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    for file in files:
        file_id.append(os.fileno(file))
    
    return file_id
