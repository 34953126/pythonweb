
#学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。
# python 最具特色的就是用缩进来写模块。
#缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

#1、行和缩进
#实例一
if True:
    print("True")
else:
    print("False")



#2、多行语句
#Python语句中一般以新行作为语句的结束符号
#但是我们可以使用斜杠（\）将一行的语句分为多行显示

#实例二
# total  = item_one + \
#          item_two + \
#          item_three

#语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday',
        'Tuesday',
        'Wednesday',
        'Thursday']

# 3、Python注释
#python中单行注释采用 # 开头。
# 第一个注释
print ("Hello, Python!")  # 第二个注释

# 4、Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
x = "a"
y = "b"

print (x,y)
