"""
是一个购物车功能，后续需要再优化一下购物车中商品数量计算的功能
"""
product_list = [
    ('iphone',10000),
    ('安卓',8000),
    ('mac pro',15000),
    ('thinkpad',8000)
]
shopping_basket = []
saving = input('请输入你的本金：')
if saving.isdigit():
    saving = int(saving)
    """
     for i,v in enumerate(product_list,1):#可以把索引一起拿出来d的函数,参数是1 就从1开始显示，如果没有参数是从0 开始，使用两个变量去接收返回，返回如下：
     1 ('iphone', 10000)
    2 ('安卓', 8000)
    3('mac pro', 15000)
    4 ('thinkpad', 8000)
    print(i,v)
    for i in enumerate(product_list,1):#可以把索引一起拿出来,参数是1 就从1开始显示，如果没有参数是从0 开始
        print(i)
    返回是4个元祖形式
    (1, ('iphone', 10000))
(2, ('安卓', 8000))
(3, ('mac pro', 15000))
(4, ('thinkpad', 8000))
    """
    while 1:
        for i,v in enumerate(product_list):#可以把索引一起拿出来,参数是1 就从1开始显示，如果没有参数是从0 开始
            print(i,'>>>>>>', v[0],v[1])
        choice = input("请输入购买商品的编号（q:退出）：")
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(product_list):
                p_info = product_list[choice]
                print('查询成功！','商品名称：',p_info[0],'商品价格：',p_info[1])
                if int(p_info[1]) <= saving:
                    saving -= int(p_info[1])
                    shopping_basket.append(p_info)
                else:
                    print('余额不足。')
            else:
                print('商品编码不存在。')
        elif choice == 'q':
            print('购买流程已退出！')
            """
            下面代码为用户展示购物车的购买商品和数量，其中统计了商品的数量，相同商品数量是加在一起的
            """
            tell_cust = []
            for i in shopping_basket:
                tell_cust.append(i[0])
            myset = set(tell_cust)
            for item in myset:
                print("购买 %s 数量： %s" % (item, tell_cust.count(item)))
            print('余额', saving)
            break #只要在某个循环体内，不管是那层嵌套里面，只要出现break 则所在的循环就退出，疑问（如果有多层循环呢，退出那一层），好像是只退出自己这一层
        else:
            print('请输入正确的商品编号。')
else:
    print('输入的本金数必须为纯正整数字，请重新输入！')