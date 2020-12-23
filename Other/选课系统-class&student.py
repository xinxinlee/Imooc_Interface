class Classes:
    """
    班级
    """
    def __init__(self,name):
        self.name = name
        self.nid = 随机字符串


class Student:
    """
    学生
    """
    def __init__(self,name,classes_name):
        self.name = name
        self.classesName = classes_name
