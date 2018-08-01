#!/usr/bin/env python

import jenkins

server_addr = 'http://localhost:800'

def listJobs(addr):
  server = jenkins.Jenkins(server_addr)
  # print server.jobs_count()


if __name__ == "__main__":
  listJobs(server_addr)
