class Foo:
    color = 'blue'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)
obj = Foo('mingming',10)

"""
下面的代码是如果没有实例就创建一个实例，然后就一直用这个实例去执行了，属于单例模式。
"""
v = None
i = 0
while i<5:
    if v:
        v.show()
    else:
        v = Foo('mingming',18)
        print('创建实例成功')
    i+=1
"""
下面代码是使用类方法和私有变量的当时来做一个可以产生实例的方法，然后如果想要用这个类的实例，只要请求这个方法就可以了
下面的obj1和obj2 是一个内存地址，所以是相当一个实例
"""
class FooClass:
    __v = None
    @classmethod
    def get_obj(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = FooClass()
            return cls.__v

obj1 = FooClass.get_obj()
print(obj1)
obj2 = FooClass.get_obj()
print(obj2)
