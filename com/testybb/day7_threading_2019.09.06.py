import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程："+self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name,self.counter,2) #调用函数执行2次退出
        #释放锁开启下一个线程
        threadLock.release()
        print("退出线程："+self.name)



def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" %(threadName,time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

#创建新线程
thread1 = myThread(1,"thread-1",1)
thread2 = myThread(2,"thread-2",2)
#开启新线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程执行完再向后执行
for t in threads:
    t.join()

print("退出线程")