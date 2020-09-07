#!/usr/bin/env python3
import shutil
import psutil
import os
import socket
import emails

def check_cpu_usage():
  """Returns True if cpu usage less than 80 %"""
  return psutil.cpu_percent(1) < 80

def check_disk_space():
  """Returns True if the disk is not full"""
  disk = "/"
  min_percent = 20
  du = shutil.disk_usage(disk)
  #Calculate the percentage of free space
  percent_free = 100*du.free / du.total
  return percent_free > 20

def check_memory_usage():
  """Returns True if available memory is more than 500MB"""
  free = psutil.virtual_memory().available
  # Convert to MB
  available_memory = (free/1024) / 1024
  return available_memory > 500

def check_resolve_hostname():
  """Returns true if localhost can be resolved to 127.0.0.1"""
  hostname = socket.gethostbyname('localhost')
  return hostname == '127.0.0.1'

def checks():
  """Checks if all the health checks functions return True(everything ok)"""
  """if not then respective error message becomes email subject"""
  if not check_disk_space():
      subject = 'Error - Available disk space is less than 20%'
      return subject
  elif not check_cpu_usage():
      subject = 'Error - CPU usage is over 80%'
      return subject
  elif not check_memory_usage():
      subject = 'Error - Available memory is less than 500MB'
      return subject
  elif not check_resolve_hostname():
      subject = 'Error - localhost cannot be resolved to 127.0.0.1'
      return subject
  else:
      return None

if __name__ == "__main__":
    USER = os.getenv('USER')
    subject = checks()
    if subject is not None:
        body = 'Please check your system and resolve the issue as soon as possible.'
        message = emails.generate_email("automation@example.com", "{}@example.com".format(USER), subject, body, "")
        emails.send_email(message)