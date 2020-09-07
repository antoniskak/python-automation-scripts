#!/usr/bin/env python3
import os
import requests
import json

path = "/home/student-02-e0e81b97de85/supplier-data/descriptions"
img_path = "/home/student-02-e0e81b97de85/supplier-data/images"

dict_keys = ["name", "weight", "description","image_name"]
my_dict = {}

for txt_file in os.listdir(path):
  key_count = 0
  fullpath = os.path.join(path,txt_file)
  respective_img = os.path.splitext(txt_file)[0]+'.jpeg'
 # print(fullpath)
 # print(respective_img)
  with open(fullpath) as f:
    for line in f:
      if key_count == 1:
        """drop the 'lbs' and convert weight value to int"""
        line = int(line.strip("lbs\n"))
      else:
        line = line.strip("\n")
      my_dict[dict_keys[key_count]] = line
      key_count +=1
    my_dict[dict_keys[3]] = respective_img
  response = requests.post("http://35.232.202.183/fruits/", data = my_dict) #requests.post path always remember last "/"
  print(response.status_code)
