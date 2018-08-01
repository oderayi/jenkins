#!/usr/bin/env python

import sys, jenkins, db
from datetime import datetime

def listJobs(addr):
  print(f"Jobs on: {addr}\n")
  server = jenkins.Jenkins(addr)
  print(server.jobs_count())


if __name__ == "__main__":
  inp = input('Enter Jenkins server address: ')
  listJobs(inp)
