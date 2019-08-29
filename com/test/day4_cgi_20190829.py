
#何为CGI
#CGI是运行在服务器上的程序，提供同客户端HTML页面的接口。它的全称是Common Gateway Interface (通用网关接口)
#CGI 程序可以是Python 脚本，Perl脚本，C或者C++程序等。换句话说，CGI程序是不限定语言的

print("Content-type:text/html \n\n")
print("Hello world!")