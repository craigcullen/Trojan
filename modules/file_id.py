import os

file_id = []

def run(**args):
    print "[*] In dirlister module."
    files = os.listdir(".")
    for file in files:
        file_id.append(file)
       
    file_1 = file_id[0]
    rfile = file_1.read()
        
    return rfile
