#!/usr/bin/python
#coding:utf-8
'''
Author:     mpsk
Date:       2016-10-06
Function:   Server for 
            Remote Connection via Proxy Server in TCP/IP Socket
Version:    1.0.3
'''
import socket
import time
import SocketServer

class target(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

class server(object):
    def __init__(self, target):
        self.target = target
        self.msglist = []
        self.sockc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def bind(self):
        self.sockc.bind((self.target.ip, self.target.port))
    def listenc(self):
        self.sockc.listen(5)
        while (True):
            conn,addr=self.sockc.accept() 
            print'Connected by',addr    
            try:
                conn.settimeout(300)
                data=conn.recv(1024)
                if(data=='quit!'):break
                else:
                    recv = data[0:8]
                    send = data[8:16]
                    #这里留下一位末位
                    msg =data[16:-1]
                    if(send != '00000000' and msg !=''):
                        self.msglist.append([recv,send,msg])
                    else:
                        #在接受者栈中寻找
                        for i in range(len(self.msglist)):
                            if(self.msglist[i][0]==recv):
                                conn.sendall('00000000' + self.msglist[i][1] + self.msglist[i][2])
                                self.msglist.pop(i)
            except socket.error:
                print 'socket time out!'
    def close(self):
        self.sockc.close()

a = server(target('localhost', 65530))
a.bind()
print "\nServer Established!"
a.listenc()
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