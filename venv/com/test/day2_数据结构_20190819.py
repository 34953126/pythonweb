import time

#列表可以装入Python的所有对象
all_in_list = [
    1,       #整数
    2.0,     #浮点数
    'ybb',   #字符串
    print('ybb'), #函数
    True,         #布尔值
    [1,2],        #列表中嵌套列表
    (3,4),        #元组
    {'ybb','922'} #字典
]

#向元组添加数据
all_in_list.insert(1,'grape')
print(all_in_list)

#字典
code = {
    'BIDU':'BaiDu',
    'SINA':'Sina',
    'YuKu':'YouKu'
}

#元组
letters = ('a','b','c','d','e','f','g')
print(letters[0])


#推导式--------------------------------------------
a = []
t0 = time.clock()
for i in range (1,20000):
    a.append(i)
print(time.clock() - t0,"seconds process time ")

t0 = time.clock()
b = [i for i in range(1,20000)]
print(time.clock()-t0,"seconds process time ")

#在Python3.7中使用 time.clock()报警告
#Python time模块之clock在Python3.3废弃，在Python3.8中将被移除
#用以浮点数计算的秒数返回当前的CPU时间，用来衡量不同程序的耗时，比time.time()更有用
# python3.3以后不被推荐使用，该方法依赖操作系统，建议使用per_counter(返回系统运行时间)或
# process_time(返回进程运行时间)代替

