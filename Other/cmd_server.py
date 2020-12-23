import socket
import subprocess

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)#等待排队的数量
print("请等待。。。")

while 1:
    conn, addr = sk.accept()  # conn就是客户端的SK 对象，addr是客户端的地址和端口
    # inp = input('青输入')#上面accept()虽然执行了，但是在阻塞状态，等对面搭上之后再执行下一行conn.send(bytes('nihao','utf-8'))语句
    '''
    conn.send(bytes('你好','utf-8'))#这个部分需要使用bytes来进行转换，socket 中传输的都是二进制格式的所以需要转一下
    #conn.send(inp)
    conn.close()#关闭某个与它通信的客户端
    sk.close()#关闭整个服务器端的通信
    '''
    #print(addr)
    while 1:
        pass
