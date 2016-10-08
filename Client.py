#!/usr/bin/python
##coding=utf-8
'''
Author:     mpsk
Date:       2016-10-06
Function:   Client for 
            Remote Connection via Proxy Server in TCP/IP Socket
Version:    1.0.3
'''
import socket
import time


class target(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class client(object):
    def __init__(self, target, myname):
        self.target = target
        self.myname = myname
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect(self):
        print 'Connecting ' + self.target.ip + ':' +str(self.target.port)
        self.sock.connect((self.target.ip, self.target.port))
    def test(self):
        self.sock.send('test')
        if(self.sock.recv(4) == "good"): print "Connection established successfully!"
        else: print "failed to connect!"
    def post(self):
        target_name = raw_input("Please input target's name:")
        msg = raw_input("Please input msg:(type 'quit!' to exit)")
        if(msg=='quit!'):
            print 'Stopped!' 
            return False
        elif(msg=='' or target_name =='00000000' or len(target_name)!=8):
            print 'invalid input!'
        else:
            #这里信息应该是8(发送者名字)+8(接收者名字)+1007(消息)+1(末位)那么长
            #返回的信息应该只有200 401 402 403 404 501 502
            #                   接受者名字   发送者名字 消息
            self.sock.sendall(target_name + self.myname + msg)      
            data = self.sock.recv(1008)    
            print data
            return True
    def request(self):
        self.sock.sendall(self.myname + '00000000')      
        data = self.sock.recv(1008)     
        print data[8:16] + ' : ' + data[16:-1] + data[-1]
        if(data !=''):
            return True
        else:
            return False
    def shutserver(self):self.sock.send('quit!')
    def close(self): self.sock.close


ip = raw_input("Please input IP Address:")
port = int(raw_input("Please input Port:"))
name = raw_input("Please input your name: (8 letters only)")
while(len(name)!=8 or name == '00000000'):
    print 'invalid input!'
    name = raw_input("Please input your name: (8 letters only)")
post = client(target(ip, port), name)
req = client(target(ip, port), name)
while(True):
    post.connect()
    req.connect()
    if(not post.post()):break
    if(not req.request()):break
    post = client(target(ip, port), name)
    req = client(target(ip, port), name)
post.close()
req.close()


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