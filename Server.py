#!/usr/bin/python
##coding = utf-8
'''
Author:     mpsk
Date:       2016-10-02
Function:   Server for 
            Remote Connection via Proxy Server in TCP/IP Socket
Version:    1.0.2
'''
import socket
import time
import SocketServer
import commands
import os

class target(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class server(object):
    def __init__(self, target):
        self.target = target
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def bind(self):
        self.sock.bind((self.target.ip, self.target.port))
    def listen(self):
        self.sock.listen(5)
        while (True):
            conn,addr=self.sock.accept() 
            print'Connected by',addr    
            try:
                conn.settimeout(300)
                data=conn.recv(1024)
                if(data=='quit!'):break
                else:##os.system(cmd) 
                
                    cmd_status,cmd_result=commands.getstatusoutput(data)   
                if len(cmd_result.strip())==0:   
                    conn.sendall('Done.')
                else:
                    conn.sendall(cmd_result)
                
            except socket.error:
                print 'socket time out!'
    def close(self):self.sock.close()

ip = raw_input("Please input IP Address:")
port = int(raw_input("Please input Port:"))
a = server(target(ip, port))
a.bind()
print "\nServer Established!"
a.listen()
a.close()
'''
def init():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost',65532))
    return sock

s = init()
s.listen(5)
while(True):
    conn,addr = s.accept()
    print 'Connection established! Client address is',addr
    try:
        conn.settimeout(2)
        buff = conn.recv(8)
        if(buff=='123456'):
            conn.send("Welcome to server!")
        elif(buff=='exit'):
            break
        else:
            conn.send("Request denied!")
    except socket.error:
        print 'Socket time out!'
    conn.close()
'''