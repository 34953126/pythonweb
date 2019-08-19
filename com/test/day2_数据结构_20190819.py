
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


all_in_list.insert(1,'grape')
print(all_in_list)