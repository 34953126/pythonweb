import socket
import sys

#编写简单的客户端连接创建的服务端，端口号为9898
#socket.connect(hosname,port) 方法打开一个TCP连接到主机为hostname端口为port的服务，连接后就可以从服务获取数据。

#创建socket对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
#设置端口号
port = 9898
#连接服务，指定主机和端口
s.connect((host,port))
#接收小于1024字节的数据
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))