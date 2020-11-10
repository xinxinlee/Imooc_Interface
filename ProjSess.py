import requests

class ProSession:
    def __init__(self):
        self.sess = requests.Session()

    def create_session(self):
        url = 'http://scm.gyl.test.9now.net/api/v1/users/login'
        headers = {'content-type': 'application/json'}
        login_data = '''{
        "shopName":"JC000327",
        "userName":"admin",
        "password":"123456",
        "authCode":"8888"
        }'''
        result = self.sess.post(url,data=login_data,headers=headers)
        return result



