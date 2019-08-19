print("练习题：")
#设计一个重量转换器，输入以‘g’数字后换算成‘kg’的值

def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(3000))

#---------------------------------------------
#设计一个求直角三角行斜边长的函数
def pythagorean_theorem(a,b):
    return  'The right triangle third side \'s length is {}'.format((a**2 + b**2) ** (1/2))
#等价于a的平方和b的平方之和1/2次方（开根）
print(pythagorean_theorem(3,4))




