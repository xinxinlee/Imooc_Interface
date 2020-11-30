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
            "青岛新村":{
                "985": "青岛东油",
                "211": "青岛农垦"
            },
            "青岛萨区":{
                "985": "青岛农大分校",
                "211": "青岛林大分校"
            }
            }
        }
    }

current_layer = Prov_dict
while True:
    for key in current_layer:
        print(key)
    choice = input("请输入名称：").strip()
    if len(choice) == 0:
        continue
    if choice in current_layer:
        current_layer = current_layer[choice]
    else:
        print("没有这个身份")

