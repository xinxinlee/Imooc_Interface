"""
输出的都是123，需要经过一层层的嵌套才能拿到最终的值
"""
class F1:
    def __init__(self):
        self.name = 123

class F2:
    def __init__(self,a):
        self.ff = a

class F3:
    def __init__(self,b):
        self.dd = b

f1 = F1()
f2 = F2(f1)
f3 = F3(f2)
#print(f2.ff.name)
#print(f3.dd.ff.name)

import sys
"""
python的编码和解码学习：
python3 中在调用encode的时候，会把数据转换为byte类型
b = byte 属于字节类型，是介于1-255之间的数字
"""
print(sys.getdefaultencoding())#打印文件的默认编码
s = "小明"#默认是unicode编码
s_to_gbk = s.encode('gbk')
b_to_uni = s_to_gbk.decode('gbk')
print(s)
print(s_to_gbk)
print(b_to_uni)