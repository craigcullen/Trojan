import os
import re

from PIL import Image

def run1(**args):
    print "[*] In login_name module."
    name = str(os.getLogin())
    return str(os.getlogin())

def run2(**args):
    print "[*] In open_jpeg module."
    pic = Image.open("/home/" + name + "/Pictures/" + re.match("^.*") + ".jpg")
    size = 120, 120
    pic.thumbnail(size)
    pic.save("/home/" + name + "/Pictures/KB" + ".thumbnail", "JPEG")
    pic.close()
    with open ("/home/" + name + "/Pictures/KB.thumbnail", "rb") as pic:
        return pic.read()