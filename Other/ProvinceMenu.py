Prov_dict={
    '黑龙江':{
        "哈尔滨":{
            "道外区":{
                "985": "哈工大",
                "211": "哈工程"
            },
            "道里区":{
                "985": "农大",
                "211": "林大"
            }
        },
        "大庆":{
            "新村":{
                "985": "东油",
                "211": "农垦"
            },
            "萨区":{
                "985": "农大分校",
                "211": "林大分校"
            }
            }
        },
    '辽宁':{
        "沈阳":{
            "沈阳一区":{
                "985": "辽宁工大",
                "211": "辽宁工程"
            },
            "沈阳二区":{
                "985": "辽宁农大",
                "211": "辽宁林大"
            }
        },
        "大连":{
            "大连新村":{
                "985": "辽宁东油",
                "211": "辽宁农垦"
            },
            "大连萨区":{
                "985": "辽宁农大分校",
                "211": "辽宁林大分校"
            }
            }
        },
    '山东':{
        "济南":{
            "济南一区":{
                "985": "济南工大",
                "211": "济南工程"
            },
            "济南二区":{
                "985": "辽宁农大",
                "211": "辽宁林大"
            }
        },
        "青岛":{
            "济南新村":{
                "985": "济南东油",
                "211": "济南农垦"
            },
            "济南萨区":{
                "985": "济南农大分校",
                "211": "济南林大分校"
            }
            }
        }
    }
#下述两个是标志位变量，用来当满足某个条件时退出某个循环
back_tag =False
exit_tag =False

while not back_tag and not exit_tag:
    for key1 in Prov_dict:
        print(key1)
    choice1 = input("请输入省份名称：").strip()
    if choice1 == 'q':
        exit_tag = True
    if choice1 in Prov_dict:
        while not back_tag and not exit_tag:
            for key2 in Prov_dict[choice1]:
                print(key2)
            choice2 = input("请输入城市名称：").strip()
            if choice2 == 'b':
                back_tag = True
            if choice2 == 'q':
                exit_tag = True
            if choice2 in Prov_dict[choice1]:
                while not back_tag and not exit_tag:
                    for key3 in Prov_dict[choice1][choice2]:
                        print(key3)
                    choice3 = input("请输入区域名称：").strip()
                    if choice3 == 'b':
                        back_tag = True
                    if choice3 == 'q':
                        exit_tag = True
                    if choice3 in Prov_dict[choice1][choice2]:
                        while not back_tag and not exit_tag:
                            for key4 in Prov_dict[choice1][choice2][choice3]:
                                print(key4)
                            choice4 = input("请输入类型名称：").strip()
                            print('the last level.')
                            if choice4 == 'b':
                                back_tag = True
                            if choice4 == 'q':
                                exit_tag =True
                        else:
                            back_tag = False
                else:
                    back_tag = False
        else:
            back_tag = False

