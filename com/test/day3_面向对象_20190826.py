import socket
class Demo:
    #类变量
    var1 = 200

    def __init__(self):
        #成员变量
        self.var2 = 200
        print("init......")

    def funcTest(self):
        #实例变量
        self.var3 = 300
        return self.var3


demo = Demo()
print(demo.funcTest())




host_name = socket.gethostname()
print(host_name)#本机名
print(socket.gethostbyname(host_name))#ipv4