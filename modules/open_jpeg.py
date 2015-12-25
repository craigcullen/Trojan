import os
from PIL import Image

def run(**args):
    print "[*] In open_jpeg module."
    kate = Image.open("/home/craig/Pictures/Kate-Beckinsale.jpg")
    kate = kate.load()
    return kate
