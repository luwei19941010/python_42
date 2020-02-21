#-*-coding:utf-8-*-
# Author:Lu Wei
import socket

sk=socket.socket()
sk.bind(('127.0.0.1',8888))
sk.listen()

conn,add=sk.accept()
print(conn)
data=conn.recv(10240)
print(data)