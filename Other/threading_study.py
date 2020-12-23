import threading,time

def addNum():
    global num
    num -= 1
    return num

num = 100
r = addNum()
print(r)

