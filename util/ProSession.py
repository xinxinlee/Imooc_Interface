import requests

class ProSession:
    """获取登录后的Session"""
    def __init__(self):
        self.session = self.create_session()

    def create_session(self):
        session = requests.Session()
        url = 'http://scm.gyl.test.9now.net/api/v1/users/login'
        headers = {'content-type': 'application/json'}
        login_data = '''{
        "shopName":"JC000327",
        "userName":"admin",
        "password":"123456",
        "authCode":"8888"
        }'''
        result = session.post(url,data=login_data,headers=headers)
        return session



