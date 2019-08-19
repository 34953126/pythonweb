print("练习题：")
#设计一个重量转换器，输入以‘g’数字后换算成‘kg’的值

def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(3000))

#---------------------------------------------
def pythagorean_theorem(a,b):
    return  'The right triangle third side \'s length is {}'.format((a**2 + b**2) ** (1/2))
#等价于a的平方和b的平方之和1/2次方（开根）
print(pythagorean_theorem(3,4))

#向文件里面写入
file = open('D:/hnxyzn/Python/work/test.txt','w')
file.write("hello world！")



