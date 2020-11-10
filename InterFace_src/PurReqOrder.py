from util.ProSession import ProSession
from util.ReadConfig import ReadIni
import requests
import json

class PurReqOrder:
    """新增采购单"""
    def __init__(self):
        self.session = ProSession().session
        self.headers = {'content-type': 'application/json'}
        self.url_add = 'http://scm.gyl.test.9now.net/api/v1/purchaseorders/beforeadd'#后续可以写在配置文件中
        self.url_purreqorder = 'http://scm.gyl.test.9now.net/api/v1/purchaseorders/add'#后续可以写在配置文件中
        self.dicadd = self.AddBillNo()

    def AddBillNo(self):
        """生成单据编号"""
        add_r = self.session.post(self.url_add,headers=self.headers)
        dicadd = json.loads(add_r.text)
        return dicadd

    def CreatPurorder(self):
        """生成采购订单"""

if __name__ == '__main__':
    obj = PurReqOrder()
    r = obj.CreatPurorder()
    print(r)