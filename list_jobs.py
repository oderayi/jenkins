import jenkins

server_addr = 'http://localhost:800'

server = jenkins.Jenkins(server_addr)
print server.jobs_count()