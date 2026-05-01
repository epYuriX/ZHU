# game/event/events.py
EVENTS = {
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
            "instant_options": [
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
            "instant_options": [
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
            "instant_options": [
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
            "instant_options": [
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
            "instant_options": [
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
            "describe": "#",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 3,
                        "yi_tie": 1,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 13
                        # 所有对手获得一异铁 - 未实现
                    },
                },
            ]
        },
        {
            "name": "富异铁区",
            "describe": "#",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 2,
                        "money": 5,
                    },
                },
            ]
        },
        {
            "name": "敌对生态圈",
            "describe": "#",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 2,
                        "score": 1,
                    },
                },
            ]
        },
        {
            "name": "洞穴和遗迹",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 5,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 10,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "yi_tie": -1,
                        # 选择一家企业 - 该玩家在此企业中的权限升一级 - 此为后续功能，暂未实现
                    },
                },
            ]
        },
        {
            "name": "荒地人村落",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 3,
                        "yi_tie": 1,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 4,
                    },
                },
            ]
        },
        {
            "name": "大型源岩场",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 5,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 4,
                        "score": 1,
                    },
                },
            ]
        },
        {
            "name": "锈锤领地",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "money": -4,
                        # 在地图上放置一个影响力 - 未实现
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 10,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 4,
                    },
                },
            ]
        },
        {
            "name": "遭弃矿场",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 4,
                    },
                },
            ]
        },
        {
            "name": "风险任务",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 3,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 4,
                    },
                },
            ]
        },
        {
            "name": "情报交换",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_shi",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        # 在此资源点(node)相邻的航道(link)上放置影响力 - 未实现
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 1,
                        "yuan_shi": 3,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 3,
                    },
                },
            ]
        },
    ],
    "lv3": [
        {
            "name": "险中净土",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "2",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 7,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 6,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "money": 6,
                        # 在此资源点或相邻的航道上放置一个影响力 - 未实现
                    },
                },
            ]
        },
        {
            "name": "高污染环境",
            "describe": "#",
            "map_attribute": {
                "resource": "yuan_yan",
                "resource_c": "2",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 2,
                        "yuan_shi": 2,
                        "yi_tie": 2,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "money": 18,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "zcys": 1,
                        "money": 4,
                    },
                },
            ]
        },
        {
            "name": "采集平台残骸",
            "describe": "#",
            "map_attribute": {
                "resource": "yi_tie",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "score": -1,
                        # 选择一家企业，升级该企业，与该企业合作一次（企业相关均为后续功能，目前略过）
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 4,
                        "yuan_shi": 3,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 4,
                        "money": 5,
                    },
                },
            ]
        },
        {
            "name": "深层矿床",
            "describe": "#",
            "map_attribute": {
                "resource": "zcys",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 1,
                        "zcys": 1,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 3,
                        "yi_tie": 2,
                    },
                },
                {
                    "id": 2,
                    "describe": "#",
                    "reward": {
                        "money": 18,
                        # 所有其他玩家获得 money*3
                    },
                },
            ]
        },
        {
            "name": "地质瑰宝",
            "describe": "#",
            "map_attribute": {
                "resource": "zcys",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yuan_shi": 1,
                        "zcys": 1,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 3,
                        "yi_tie": 3,
                    },
                },
            ]
        },
        {
            "name": "裂谷矿脉",
            "describe": "#",
            "map_attribute": {
                "resource": "zcys",
                "resource_c": "1",
            },
            "instant_options": [
                {
                    "id": 0,
                    "describe": "#",
                    "reward": {
                        "yi_tie": 1,
                        "zcys": 1,
                    },
                },
                {
                    "id": 1,
                    "describe": "#",
                    "reward": {
                        "yuan_yan": 3,
                        "yuan_shi": 3,
                    },
                },
            ]
        },
    ]
}
