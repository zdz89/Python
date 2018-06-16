import PIL
from PIL import Image
import os

wymiar1 = 128

os.chdir(r"C:\Users\KEO\Desktop\python")
for nazwa in os.listdir("."):
  if nazwa.endswith(".JPG"):
    outfile = nazwa.split(".")[0] + ".ICO.JPG"
    img = Image.open(nazwa)

    if img.size[0] > img.size[1]:
        wpercent = (wymiar1/float(img.size[1]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((hsize,wymiar1))
    else:
        wpercent = (wymiar1/float(img.size[0]))
        hsize = int((float(img.size[0])*float(wpercent)))
        img = img.resize((wymiar1,hsize))

    img = img.crop((0,0,128,128))
    img = img.rotate(180)
    img = img.convert("L")
    img.save(outfile)
