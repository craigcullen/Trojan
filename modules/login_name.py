import os

def run(**args):
    print "[*] In login_name module."
    return str(os.getlogin())
