from PIL import Image

def run(**args):
    print "[*] In open_jpeg module."
    with Image.open("/home/craig/Pictures/Kate-Beckinsale.jpg") as kate: 
        size = 120, 120
        katethumb = kate.thumbnail(size)
        return str(katethumb.read())
