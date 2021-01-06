#类的对象的属性和类的方法的相关的学习
'''
class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def fuc1(self,a,b):
        sum = a+b
        return sum


obj = Foo('mingming',18,)

#r = getattr(obj,'fuc1')
res = getattr(obj,'fuc1')(3,4)#使用getatter这个函数用来取出类的实例中的属性和类的方法，当取出的是实例的属性就可以直接应用，取出的是方法就按照方法的格式执行就可以
print(res)
r = hasattr(obj,'fuc1')#用来判断类的实例或者类中是否有某个属性、方法
print(r)
setattr(obj,'color','blue')#给类的实例添加属性，其实是放在了对象的内存中了，在类的内存中是没有这个属性的
print(obj.color)
delattr(obj,'color')#删除属性,不可以删除类的方法
print(obj.color)
'''
#类的属性和类的方法的相关学习
class Foo:
    color = 'blue'
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj = Foo('mingming',10)
r = getattr(obj,'color')#类的静态属性也是可以通过getattr函数拿到的
print(r)
'''
其中这个对象，是指任何对象，也可以是一个模块，就是直接把模块导入进来后，这个模块就跟上面的类一样了，写在第一个参数的位置，后面是这个模块中含有的方法或者属性
如getattr(模块名，'模块的方法或属性')
总结，getattr()需要的参数是一个对象，一个对象中的属性或者方法，其中这个对象的含义是：
1、如果在本文件内，那对象就是这个类的实例
2、如果在本文件外引入了其他.py 文件后，这个文件就是一个实例，比如xx.py 这个xx 就是这个函数中的实例位置的参数，后面的参数就可以是xx 文件中的类、
和类这个级别平级的函数和变量，都可以。
3、关于反射的应用 传入一个字符串作为第二个参数，根据这个参数去找对应的方法去，然后去执行就可以执行那个方法，比如web框架，客户端会传一下字符串个后端，后端根据传入的
内容去找对应的代码然后去执行。
'''
