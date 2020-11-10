import configparser

class ReadIni:
    """读取配置文件"""
    def __init__(self,file_name,node):
        self.cf = self.load_ini(file_name)
        self.node = node

    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf

    def get_value(self,element_name):
        element = self.cf.get(self.node,element_name)
        return element

if __name__ == '__main__':
    file_name = 'D:\\Imooc_Interface\\config\\ReqData.ini'
    read_obj = ReadIni(file_name,'PurReqOrder')
    a = read_obj.get_value('data')
    print(a)
    print(type(a))


