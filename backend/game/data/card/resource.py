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
            "describe": "你手拿着荒地人向导倒卖的旧地图，到达了标记有源石矿藏的位置，但那儿的源石早已不知去向。在注意到地图下角的绘制日期后，你不禁顿足准备破口大骂。但鞋底踩上的那些带有小孔的松软土壤，倒也不算是空手而归。",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "现在就装一车源岩回城",
                    "reward": {
                        "yuan_yan": 4,
                    },
                },
                {
                    "id": 1,
                    "describe": "迫使卖给你“过期地图”的家伙弥补损失",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
            ]
        },
        {
            "name": "清理虫巢",
            "describe": "#",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "向当地治安官邀功",
                    "reward": {
                        "money": 7,
                    },
                },
                {
                    "id": 1,
                    "describe": "附近聚落居民向你表达感谢",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
            ]
        },
        {
            "name": "废弃矿坑",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "先把矿井外留下的资源设备收走",
                    "reward": {
                        "yi_tie": 2,
                        "money": 2,
                    },
                },
                {
                    "id": 1,
                    "describe": "“看看你们干的好事！”天黑前要是不把这挖通我就把你们活埋在源岩里！",
                    "reward": {
                        "yuan_yan": 4,
                    },
                },
            ]
        },
        {
            "name": "矿业聚落",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 7
                    },
                },
            ]
        },
        {
            "name": "外露矿床",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 4,

                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
            ]
        },
    ],
    "lv2": [
        {
            "name": "异铁开采权",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [  # 选择战吼触发
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 4,

                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 3,
                    },
                },
            ]
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
