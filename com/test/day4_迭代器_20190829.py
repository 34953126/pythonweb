import sys #引入sys模块


list=[1,2,3,4,5]
it =iter(list) #创建迭代器对象

# print(next(it)) #输出跌代器的下一个元素
# print(next(it))

#全部输出
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# ----------------------------------------------------------------------------------------------------


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(str(next(myiter))+"---")
print(next(myiter))
print(next(myiter))
print(next(myiter))
