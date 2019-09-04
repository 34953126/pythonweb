#1、首先导入mysql驱动器。解决办法：File-->Settings-->project interpreter-->双击pip--->搜索mysql-connector-python
# 鼠标选中mysql-connector-python--->点击左下角Install Package




import mysql.connector

# 创建数据库连接
# mydb = mysql.connector.connect(
#     host="localhost",   #数据库主机地址
#     user="test",        #数据库用户名
#     password="test",       #数据库密码
#     port="3306",
#     database="test"
# )

conn = mysql.connector.connect(
    host='localhost',
    user='test',
    password='test',
    auth_plugin = 'mysql_native_password'
)

print(conn)

