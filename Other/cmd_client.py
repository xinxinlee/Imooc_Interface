import socket
import os

sk = socket.socket()
address = ('127.0.0.1', 8000)
sk.connect(address)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
'''
data = sk.recv(1024)#一次最大收1024,这个收的动作一直在等待中，对面过来数据后会自动显示
print(str(data,'utf-8'))#是一个byte 类型的所以打印出来是b'\xe4\xbd\xa0\xe5\xa5\xbd'这种形式的，所以需要在接受后进行解码和转换成字符串

sk.close()#关闭此客户端的连接，只需要关闭SK就行了
'''
while 1:
    inp = input('>>>>>').strip()
    cmd,path = inp.split('|')
    path = os.path.join(BASE_DIR,path)
    filename =




sk.close()
