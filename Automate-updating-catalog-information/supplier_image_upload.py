#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

path = "/home/student-02-e0e81b97de85/supplier-data/images"

for file in os.listdir(path):
  if ".jpeg" in os.path.basename(file):
    fullpath = os.path.join(path,file)
    with open(fullpath, "rb") as opened:
      response = requests.post(url, files={'file': opened})
      print(response.status_code)
