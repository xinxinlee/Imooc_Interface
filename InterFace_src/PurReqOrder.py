from util.ProSession import ProSession
from util.ReadConfig import ReadIni
import requests
import json

class PurReqOrder:
    """新增采购单"""
    def __init__(self):
        self.session = ProSession().session
        self.headers = {'content-type': 'application/json'}
        self.url_add = self.ReadConfig()['url_add']
        self.url_purreqorder = self.ReadConfig()['url_purreqorder']
        self.PurReqOrder_data = self.ReadConfig()['PurReqOrder_data']
        self.dicadd = self.AddBillNo()

    def ReadConfig(self):
        """读取配置文件的内容"""
        result_dict = {}
        file_name = 'D:\\Imooc_Interface\\config\\ReqData.ini'
        cof_obj = ReadIni(file_name, 'PurReqOrder')
        result_dict['url_add'] = cof_obj.get_value('url_add')
        result_dict['url_purreqorder'] = cof_obj.get_value('url_purreqorder')
        result_dict['PurReqOrder_data'] = cof_obj.get_value('PurReqOrder_data')
        #print(result_dict)
        return result_dict

    def AddBillNo(self):
        """生成单据编号"""
        add_r = self.session.post(self.url_add,headers=self.headers)
        dicadd = json.loads(add_r.text)
        return dicadd

    def CreatPurorder(self):
        """生成采购订单"""
        PurReqOrder_data = self.PurReqOrder_data
        PurReqOrder_data["fsBillTime"]= self.dicadd["data"]["document_time"]
        PurReqOrder_data["fsDeliveryDate"] = self.dicadd["data"]["document_time"]
        PurReqOrder_data["fsPurchaseOrderId"] = self.dicadd["data"]["document_code"]
        r = self.session.post(self.url_purreqorder,data=PurReqOrder_data,headers=self.headers)
        res = json.loads(r.text)
        return res

if __name__ == '__main__':
    obj = PurReqOrder()
    #r = obj.ReadConfig()
    r = obj.CreatPurorder()
    print(r)