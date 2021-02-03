from util.Httprequests import myrequests

url = "http://kt-test.st.9now.net/orderCenter/esb-fadada/verifyNotify"
obj = myrequests(url)
data = {"appId":"900001","serialNo":"5ae85dc2ddd948b5a8218de8a8e21cf8","customerId":"3E0A88FA5F8261DD","status":"2","statusDesc":"测试"}
result = obj.mypost(data)
print(result)
