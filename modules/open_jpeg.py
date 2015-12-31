from PIL import Image

def run(**args):
    print "[*] In open_jpeg module."
    kate = Image.open("/home/craig/Pictures/Kate-Beckinsale.jpg")
    size = 120, 120
    kate.thumbnail(size)
    kate.save("/home/craig/Pictures/KB" + ".thumbnail", "JPEG")
    kate.close()
    with open ("/home/craig/Pictures/KB.thumbnail", "rb") as kate:
        return kate.read()

