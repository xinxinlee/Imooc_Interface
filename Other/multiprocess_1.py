from multiprocessing import Process
import time
#一种直接使用多进程函数的方法
def f(name):
    time.sleep(1)
    print('hello',name,time.ctime())

if __name__ == '__main__':
    p_list = []
    for i in range(5):
        p = Process(target=f,args=('xiaoming',))
        p_list.append(p)
        p.start()
    #for p in p_list:
        #p.join()
    print('我是主进程')


#还有另外一种使用类方式的多进程方法

