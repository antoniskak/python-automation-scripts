#!/usr/bin/env python3
import os
import reports
import sys
from datetime import date
import emails

path = "/home/student-02-e0e81b97de85/supplier-data/descriptions"

def main(argv):
  """
  Creates string to pass the report into the following format:

  name: Apple

  weight: 500 lbs

  [blank line]
  """
  string = ""
  for file in os.listdir(path):
    fullpath = os.path.join(path,file)
    with open(fullpath) as text_file:
      count = 0
      for line in text_file:
        if count == 0:
          string += "name: {}".format(line)+"<br/>"
          count+=1
        elif count == 1:
          string += "weight: {}".format(line)+"<br/>"
          count +=1

  """Generates the report"""
  paragraph = string
  print(paragraph)
  attachment = "/tmp/processed.pdf"
  today = date.today()
  today_format = today.strftime("%B %d, %Y")
  title = "Processed Update on: {}".format(today_format)
  reports.generate_report(attachment, title, paragraph)

  """Generates and sends the email"""
  sender = "automation@example.com"
  recipient = "student-02-e0e81b97de85@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"
  message = emails.generate_email(sender, recipient, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main(sys.argv)
