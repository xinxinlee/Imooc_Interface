'''
dict1 = str({'name':'xiaoming','age':18,'color':'blue'})

f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','w')
f.write(dict1)
f.close()

f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','r')
data = f.read()#data此时是str
data_new = eval(data)#使用eval（）函数把str 变成dict
print(type(data_new))
print(data_new['name'])
"""
由上面例子可以看出，字典不可以直接存储在文本里，需要转化成字符串后才能写到文本中，而从文本中取出来的数据也都是字符串类型
的，要想变成字典这种结构的也需要再转化。所以开发语言中都有通用的一个过程就是序列化和反序列化。
序列化，就是把对象或者变量从内存中取出然后转化成可以传输或者存储的格式的过程，反序列化就是反之。
pickling 和unpickling
"""

import json

dict2 = {'name':'xiaotu','age':18,'color':'blue'}
f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','w')
f.write(json.dumps(dict2))
f.close()

f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','r')
data1 = f.read()
data_res = json.loads(data1)
print(data_res['name'])
"""
以上是JSON 模块提供的方法来实现相同的功能，JSON只能处理列表、字典等一些常规数据类型的序列化操作，函数也类的序列化就无法
使用了，需要用到另外一个模块pickle来实现对类和函数的序列化操作
"""

import pickle

def fuc1():
    print('hello')

class Test1:
    def __init__(self):
        pass
    def fuc1(self):
        pass

obj = Test1()

res = pickle.dumps(fuc1)
f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','wb')
f.write(res)
f.close()

f1 = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','rb')
res = f1.read()
re_res = pickle.loads(res)
print(re_res)
"""
pickle 中也是有两个同json一样的方法，不仅可以操作常规数据类型，还可以操作函数、对象和类，如果做文本读写，打开文件时需要使用'wb'
和'rb'的模式，这是pickle模块的特点
"""

import json

"""
以上是关于dump和load的学习，同dumps和loads比起来，dunp和load减少了读和写两部分，以dump 为例。
"""
dict2 = {'name':'xiaotu','age':18,'color':'blue'}
f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','w')
json.dump(dict2,f)#在序列化的同时直接把内容写进去了
f.close()

f = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','r')
data_res = json.load(f)#直接把文件中的内容发序列化和读出来
print(data_res['name'])
'''

import shelve

f = shelve.open('D:\Imooc_Interface\Other\ProvinceMemuNew')
f['info'] = {'name':'xiaotuzi','age':'20'}#会生成三种格式的文件
print(f['info'])