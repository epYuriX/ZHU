# game / data / card / resource.py
RESOURCE_CARDS = {
    "lv1": [
        {
            "name": "中立采石场",
            "describe": "带着补给的武装车队旁若无人地驶入了这座早期勘探队伍建立的采石场。“我们只效劳于金券，不会效忠于任何当地竞争者！”这座采石场的领导人向你的人马喊道。",
            "map_attribute": {  # 资源类型 / 资源乘数
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "“我们只是过来兑换一些燃料，并谈谈生意”",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "“今天起这里不再由你说了算了”",
                    "reward": {
                        "yi_tie": 2,
                        "money": 2,
                    },
                },
            ]
        },
        {
            "name": "富饶岩层",
            "describe": "",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "name": "",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
                {
                    "id": 1,
                    "name": "今天起这里不再由你说了算了",
                    "reward": {
                        "yi_tie": 2,
                        "money": 2,
                    },
                },
            ]
        },
    ],
    "lv2": [
        {
            "name": "",
            "map_attribute": {
                "resource": "",
                "resource_c": "",
            },
            "instant_bonus": {
                "money": 0,
                "yuan_yan": 0,
                "yuan_shi": 0,
                "yi_tie": 0,
                "zcys": 0
            }
        },
        {
            "name": "",
            "map_attribute": {
                "resource": "",
                "resource_c": "",
            },
            "instant_bonus": {
                "money": 0,
                "yuan_yan": 0,
                "yuan_shi": 0,
                "yi_tie": 0,
                "zcys": 0
            }
        },
    ],
    "lv3": [
        {
            "name": "",
            "map_attribute": {
                "resource": "",
                "resource_c": "",
            },
            "instant_bonus": {
                "money": 0,
                "yuan_yan": 0,
                "yuan_shi": 0,
                "yi_tie": 0,
                "zcys": 0
            }
        },
        {
            "name": "",
            "map_attribute": {
                "resource": "",
                "resource_c": "",
            },
            "instant_bonus": {
                "money": 0,
                "yuan_yan": 0,
                "yuan_shi": 0,
                "yi_tie": 0,
                "zcys": 0
            }
        },
    ]
}
