import os
import re

from PIL import Image

def run(**args):
    print "[*] In login_name module."
    name = str(os.getlogin())
    return str(os.getlogin())
    print "[*] In open_jpeg module."
    pic = Image.open("/home/" + name + "/Pictures/" + re.match("^.*") + ".jpg")
    size = 120, 120
    pic.thumbnail(size)
    pic.save("/home/" + name + "/Pictures/KB" + ".thumbnail", "JPEG")
    pic.close()
    with open ("/home/" + name + "/Pictures/KB.thumbnail", "rb") as pic:
        return pic.read()