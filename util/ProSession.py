import requests
from util.ReadConfig import ReadIni

class ProSession:
    """获取登录后的Session"""
    def __init__(self):
        self.session = self.create_session()

    def create_session(self):
        session = requests.Session()
        file_name = 'D:\\Imooc_Interface\\config\\ReqData.ini'
        cof_obj = ReadIni(file_name,'logSession')
        url = cof_obj.get_value('url_login')
        login_data = cof_obj.get_value('login_data')
        headers = {'content-type': 'application/json'}
        result = session.post(url,data=login_data,headers=headers)
        return session
