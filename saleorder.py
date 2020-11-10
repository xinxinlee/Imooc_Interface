import requests
import json
import random
from ProjSess import ProSession

#先定义一个有Session功能的对象
session_obj = ProSession()
session_obj.create_session()
session_log = session_obj.sess
headers = {'content-type': 'application/json'}
#连续生成采购单,用while 循环实现
t = 0
while t < 1:
    add_url = 'http://scm.gyl.test.9now.net/api/v1/purchaseorders/beforeadd'
    radd = session_log.post(add_url,headers = headers)
    dicadd = json.loads(radd.text)
    print(dicadd["data"]["document_code"])
    print(dicadd["data"]["document_time"])


#连续生成多张采购入库单
	#当参数结构比较复杂的时候，而且参数中key和value用中文的时候，还是要用dumps来把字段转换为字符串比较安全和方便
    json_rukudata = json.dumps({
	"fsBillTime": dicadd["data"]["document_time"],
	"fsSupplierName": "2.9供应商1",
	"fsAddress": "ghjhkl",
	"fsRemark": "",
	"fsStaffId": "",
	"fsDeliveryDate": dicadd["data"]["document_time"],
	"fiDocumentStatus": 1,
	"fsCellphoneCt": "17621735262",
	"fsContact": "",
	"fsSupplierId": "002",
	"fiStatus": "1",
	"fiSourceType": "",
	"fsDepartmentId": "",
	"fsPurchaseOrderId": dicadd["data"]["document_code"],
	"list": [{
		"fsApplicationUnitId": "",
		"fdMoney": "2500.00",
		"fsDetailedNotes": "",
		"fdTotalTax": "2500.00",
		"fsOrderUnit": "箱",
		"fdNumber": "100.00",
		"fsPkNo": "4d1e504e-3527-499e-8682-85a3b6a933a1",
		"fdPrice": "25.00",
		"fsUnitId": "002",
		"fdTax": "0.00",
		"fdValueAddRate": "0.00",
		"fsMaterialId": "001",
		"fsSourceEntryNumber": "",
		"fiEntryNumber": 1,
		"is_editable": "true",
		"fsSingleSourceNumber": "",
		"fdTaxPrice": "25.00",
		"fsModelno": "5kg/箱",
		"fsMaterialName": "土豆"
	}, {
		"fsApplicationUnitId": "",
		"fdMoney": "9500.00",
		"fsDetailedNotes": "",
		"fdTotalTax": "9500.00",
		"fsOrderUnit": "箱",
		"fdNumber": "100.00",
		"fsPkNo": "b3f83653-cb81-4502-8291-f5ad56ff53e2",
		"fdPrice": "95.00",
		"fsUnitId": "002",
		"fdTax": "0.00",
		"fdValueAddRate": "0.00",
		"fsMaterialId": "002",
		"fsSourceEntryNumber": "",
		"fiEntryNumber": 2,
		"is_editable": "true",
		"fsSingleSourceNumber": "",
		"fdTaxPrice": "95.00",
		"fsModelno": "   ",
		"fsMaterialName": "鸡肉"
	}, {
		"fsApplicationUnitId": "",
		"fdMoney": "39500.00",
		"fsDetailedNotes": "",
		"fdTotalTax": "39500.00",
		"fsOrderUnit": "箱",
		"fdNumber": "100.00",
		"fsPkNo": "aab1f68b-4dbe-444f-9ad1-e35bce9bb609",
		"fdPrice": "395.00",
		"fsUnitId": "002",
		"fdTax": "0.00",
		"fdValueAddRate": "0.00",
		"fsMaterialId": "003",
		"fsSourceEntryNumber": "",
		"fiEntryNumber": 3,
		"is_editable": "true",
		"fsSingleSourceNumber": "",
		"fdTaxPrice": "395.00",
		"fsModelno": "   ",
		"fsMaterialName": "牛肉"
	}]
})
    rruku = session_log.post('http://scm.gyl.test.9now.net/api/v1/purchaseorders/add',data=json_rukudata,headers=headers)
    dicruku = json.loads(rruku.text)
    print(dicruku)
    t += 1
