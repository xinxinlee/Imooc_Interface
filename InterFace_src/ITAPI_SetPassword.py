from util.Httprequests import myrequests
from util.Excelreader import ExcelDate
import xlsxwriter as xw

#读Excel获取请求参数
def get_data(data_path,sheetname):
    readExcel_obj = ExcelDate(data_path,sheetname)
    data_list = []
    for i in range(1,readExcel_obj.nrows):
        data = readExcel_obj.get_col_value(i,1)
        data_list.append(data)
    return data_list
#使用参数进行POST请求
def api_setpassword(url,data):
    post_obj = myrequests(url)
    api_result = post_obj.mypost(data)
    return api_result


def write_value(path,col,value):
    workbook = xw.Workbook(path)
    worksheet = workbook.add_worksheet()
    worksheet.write(col, value)
    workbook.close()

if __name__ == '__main__':
    data_path = "D:\\Imooc_selenium\\config\\case.xlsx"
    sheetname = "logincase"
    url = 'http://10.1.219.12:7017/ad/resetPWD'
    r_api_list = []
    r_list = get_data(data_path,sheetname)
    for data in r_list:
        #print(data)
        r_api = api_setpassword(url,data)
        #print(r_api)
        r_api_list.append(r_api)
    print(r_api_list[0]["sysErrDesc"])
    path = 'D:\\Imooc_selenium\\config\\test_result.xlsx'
    for r_i in range(0,len(r_api_list)):
        values = r_api_list[r_i]["sysErrDesc"]
        write_value(path,'A1',values)

