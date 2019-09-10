import time
import calendar

ticks = time.time()
print("当前时间戳为:",ticks)

localtime =  time.localtime(time.time())
localtime = time.asctime(time.localtime(time.time()))
print("本地时间为：",localtime)

#格式化时间(2019-09-10 11:35:16)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

#日历
cal = calendar.month(2019,9)
print("以下输出2019年9月的日历")
print(cal)