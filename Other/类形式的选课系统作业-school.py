import pickle

class School:
    def __init__(self,name):
        self.name = name
        self.唯一标识 = '随机字符串'
    def save(self):
        """
        正常情况下一个类的被实例化之后是保存在内存中的，我们可以使用pickle模块把类保存在某个文本中
        """
        pickle.dump((open(self.学校的唯一标识),'wb'),self)#用pickle 的dump 方法来把对象保存在文件中，其中self 就代表是类的实例，调用这个方法实例就可以把自己写到某个文件中

    def __str__(self):
        """
        这个函数用来实现，当打印一个对象的时候就会把对象的name 属性打印出来
        :return:
        """
        return self.name

    @staticmethod
    def get_all():
        """
        这是一个获取所有存在文件中对象，并且返回一个列表的方法，因为不需要知道具体是哪个对象所以函数中不需要self，直接在类中把这个函数设置类方法，使用类名就可以直接调用了
        主要是返回上面写进去的所有的实例，写进去再读出来
        """
        obj_list = []
        for item in range(xx):
            obj = pickle.load(item)
            obj_list.append(obj)
        return obj_list



s1 = School('上海')
s2 = School('北京')