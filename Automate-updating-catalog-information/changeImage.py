#!/usr/bin/env python3
import os
from PIL import Image

path = "/home/student-02-e0e81b97de85/supplier-data/images"

for file in os.listdir(path):
  base = os.path.basename(file)
  fullpath = os.path.join(path, file)
  if ".tiff" in base:
    im = Image.open(fullpath)
    # The raw images from images subdirectory contains alpha transparency layers
    # So we first convert RGBA 4-channel to RGB 3-channel format
    im_new = im.resize((600,400)).convert("RGB")
    # name without the extention
    name = os.path.splitext(base)[0]
    # add ".jpeg" extention
    new_file = path + "/" + name + ".jpeg"
    im_new.save(new_file, "JPEG")

