import base64
from PIL import Image

def run(**args):
    print "[*] In open_jpeg module."
    with open("/home/craig/Pictures/Kate-Beckinsale.jpg","rb") as kate_image:
        kate_image = base64.b64encode(kate_image.read()) 
    return kate_image
