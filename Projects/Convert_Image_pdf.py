import sys
import img2pdf
import os
from PIL import Image

filepath1 = Image.open("filepath")
if os.path.isdir(filepath1):
    with open("output.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath1):
            if not fname.endswith(".jpg"):
                continue
            path = os.path.join(filepath1, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
elif os.path.isfile(filepath1):
    if filepath1.endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath1))
else:
    print("please input file or dir")