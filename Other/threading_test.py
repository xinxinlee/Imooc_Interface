import threading,time
"""
def music(func):
    for i in range(2):
        print("I am listening to %s.%s"%(func,time.ctime()))
        time.sleep(2)
        print("music 的 end listen %s" %time.ctime())

def movie(func):
    for i in range(2):
        print("I am at the %s. %s" %(func,time.ctime()))
        time.sleep(5)
        print("end listen %s" %time.ctime())

threads = []
t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('世界末路',))
threads.append(t2)


if __name__ == '__main__':
    for t in threads:
        t.start()
        #t.join()加载这个位置的作用就是串行，第一个函数执行完毕后，被join 阻塞住了，等第一个彻底执行完毕后，才能执行第二个

    #t.join()
    print('over %s' %time.ctime())

"""
class MyThread(threading.Thread):

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run (self):
        """
        这里面就是要执行的部分，写在这个run方法中
        :return:
        """
        print("running on number:%s" %self.num)
        time.sleep(3)

if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()