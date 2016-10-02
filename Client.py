#!/usr/bin/python
##coding=utf-8
'''
Author:     mpsk
Date:       2016-10-02
Function:   Client for 
            Remote Connection via Proxy Server in TCP/IP Socket
Version:    1.0.2
'''
import socket
import time


class target(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class session(object):
    def __init__(self,target):
        self.target = target
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        print 'Connecting ' + self.target.ip + ':' +str(self.target.port)
        self.sock.connect((self.target.ip, self.target.port))
    def establish(self):
        self.sock.send('123456')
        if(self.sock.recv(20) == "Welcome to server!"): print "Connection established successfully!"
        else: print "failed to connect!"
    def command(self):
            cmd=raw_input("Please input cmd:")
            if(cmd=='quit!'):
                print 'Stopped!' 
                return False
            else:
                self.sock.sendall(cmd)      
                data=self.sock.recv(1024)     
                print data
                return True
    def shutserver(self):self.sock.send('quit!')
    def close(self): self.sock.close

ip = raw_input("Please input IP Address:")
port = int(raw_input("Please input Port:"))
b = session(target(ip, port))
while(True):
    b.connect()
    if(not b.command()):break
    b = session(target(ip, port))
b.close()
'''
##Legacy TCP/IP

def init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock

s = init()
s.connect(('localhost',65532))

time.sleep(2)
s.send('exit')
print s.recv(20)
s.close
'''