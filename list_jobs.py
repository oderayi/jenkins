#!/usr/bin/env python

import sys, jenkins, db
from datetime import datetime

def listJobs(addr):
  server = jenkins.Jenkins(addr)
  jobs = server.get_jobs()
  print(f"Jobs on: {addr}\n")
  print(jobs)
  storeJobs(jobs)

def storeJobs(jobs):
  dbHandle = db()
  conn = db.init()
  for job in jobs:
    db.insert(conn, [job.name, datetime.now])


if __name__ == "__main__":
  inp = input('Enter Jenkins server address: ')
  listJobs(inp)
