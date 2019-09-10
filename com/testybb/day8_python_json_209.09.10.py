import json

#字典类型转换为json对象
data ={
    'no':1,
    'name':'baidu',
    'url':'http://www.baidu.com'
}

json_str = json.dumps(data)
print("Python原始数据："+repr(data))
print("Json对象",json_str)
print("data['name']===",data['name'])