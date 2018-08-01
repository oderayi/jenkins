#!/usr/bin/env python

import sys, jenkins

server_addr = 'http://localhost:800'

def listJobs(addr):
  print("Jobs: \n")
  server = jenkins.Jenkins(server_addr)
  print(server.jobs_count())


if __name__ == "__main__":
  inp = raw_input('Enter Jenkins server address: ')
  print(inp)
  listJobs(server_addr)
