from PIL import Image

def run(**args):
    print "[*] In open_jpeg module."
    with open("/home/craig/Pictures/Kate-Beckinsale.jpg","rb") as kate_image: 
        return kate_image.read()
