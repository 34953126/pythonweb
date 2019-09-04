#1、首先导入mysql驱动器。解决办法：File-->Settings-->project interpreter-->双击pip--->搜索mysql-connector-python
# 鼠标选中mysql-connector-python--->点击左下角Install Package


import mysql.connector
# 创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",   #数据库主机地址
    user="root",        #数据库用户名
    password="123",     #数据库密码
    port="3340",        #数据库端口
    database="test"     #数据库名
)
print(mydb)

#创建表
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))") #（只需运行一次）

#查看所有表
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

#设置主键
#mycursor.execute(" ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY ")#（只需运行一次）

#插入数据
# sql = "insert into sites (name,url) values (%s,%s)"
# val = ("baidu","http://www.baidu.com")
# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"记录插入成功")

#批量插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]
mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")
print("Id:",mycursor.lastrowid)#获取id

#查询数据
mycursor.execute("select * from sites")
myresult = mycursor.fetchall()
for y in myresult:
    print(y)
