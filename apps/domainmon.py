'''
import time
while True:
    print('iki crot')
    time.sleep(2)
'''
import os

os.system('apk add openssh-client')
os.system('ssh -o ServerAliveInterval=30 -o TCPKeepAlive=yes -o StrictHostKeyChecking=no -R  5555:0.0.0.0:8081 rizoa@145.239.233.184')