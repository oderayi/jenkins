import jenkins

server = jenkins.Jenkins('http://localhost:8000')
print server.jobs_count()