"""
读一个文件，read()有参数是来限制读出来的字符数，英文和中文都是相同的字符个数，读完之后关闭整个文件
file_prov = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','r',encoding='utf-8')
#print(file_prov.read(200))
file_prov.close()

file_prov = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','w',encoding='utf-8')#当使用写模式打开一个文件的时候就已经把此文件内容清空了,同时如果文件名不存在也会新建一个文件
file_prov.write('hhh')

file_prov.write('heihei')
#上面两个语句的写在文件中结果是：hhhheihei 要想换行可以这么写：在两句之间写file_prov.write('\n')
file_prov.close()

file_prov = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','a',encoding='utf-8')
file_prov.write('\n 轻舟已过万重山')
file_prov.close()
#关于写进去的时机问题，如果在close 之前叫一个等待时机，比如说等待10秒，在等待的结束前还是没有真正写入内容，只是暂存在缓存区，在这个等待的过程中是可以另外再读写的。不知道是不是可以同时写
"""
file_prov = open('D:\Imooc_Interface\Other\ProvinceMemu.txt','r',encoding='utf-8')
#line = file_prov.readline()#读第一行
line = file_prov.readlines()#f返回['hhhheiheihhh轻舟已过万重山\n', ' 轻舟已过万重山']
num = 0
for i in line:
    num += 1
    if num ==3:
        print(i.strip(),'我是新增的内容')
    else:
        print(i.strip())
file_prov.close()

