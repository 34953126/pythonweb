#导入socket、sys模块
import socket
import sys

#socket.socket([family[, type[, proto]]])
#family ：套接字家族可以使AF_UNIX或者AF_INET
#type   ：套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
#protocol：一般不填默认为0


#创建socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
port = 9898
#绑定端口号
serversocket.bind((host,port))
#设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    #建立客户端连接
    clientsocket,addr = serversocket.accept()
    print("连接地址：%s" %str(addr))
    #发送数据到客户端
    msg = '欢迎访问！'+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()