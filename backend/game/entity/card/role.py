# game/data/card/role.py
"""
    ROLE_CARDS[] 角色列表
        id: 角色 id
        name: 角色名
        enterprise: 是否为企业拓展角色
        camp: 阵营
        describe: 描述
        skill[]: 技能列表
            type: 技能分类
            name: 技能名
            describe: 技能描述
"""
ROLE_CARDS = [
    {
        "id": 1,
        "name": "极境",
        "enterprise": False,
        "camp": "dafault",
        "describe": "罗德岛特派联络员。",
        "skill": [
            {
                "type": "策略",
                "name": "后勤调遣",
                "describe": "从你拥有数量最少的[源岩][源石][异铁]中选择 1 种, 获得 4 个该资源。"
            },
            {
                "type": "计谋",
                "name": "导航通讯",
                "describe": "支付 3[源石], 选择一个相邻且有自己影响力的资源点, 以该资源点为目标, 免费[城市移动]。"
            },
        ]
    },
    {
        "id": 2,
        "name": "德克萨斯",
        "enterprise": False,
        "camp": "dafault",
        "describe": "企鹅物流优秀员工。",
        "skill": [
            {
                "type": "策略",
                "name": "特别递送",
                "describe": "获得 12[货币], 选择一张设施供应区的设施牌, 将其移至设施牌堆底。"
            },
            {
                "type": "计谋",
                "name": "叙拉古人",
                "describe": "支付 3[货币], [移除影响力][移动影响力][移动影响力]。"
            },
        ]
    },
    {
        "id": 3,
        "name": "雷蛇",
        "enterprise": False,
        "camp": "dafault",
        "describe": "黑钢国际的B.P.R.S特派干员。",
        "skill": [
            {
                "type": "策略",
                "name": "安保协议",
                "describe": "[放置影响力][放置影响力], 本回合[收尾阶段]移除 1 个你的影响力。"
            },
            {
                "type": "计谋",
                "name": "控制阵地",
                "describe": "支付 3[货币], [替换影响力]。"
            },
        ]
    },
    {
        "id": 4,
        "name": "坎诺特",
        "enterprise": False,
        "camp": "dafault",
        "describe": "游弋于泰拉各地的生意人。",
        "skill": [
            {
                "type": "策略",
                "name": "贸易渠道",
                "describe": "将任意资源按以下单价[出售]:"
                            "[源岩]: 3[货币], [源石]: 3[货币]"
                            "[异铁]: 4[货币], [至纯源石]: 15[货币]"
            },
            {
                "type": "计谋",
                "name": "征收物资",
                "describe": "从[源岩][源石][异铁]中选择一种, [所有玩家]以 2[货币]的单价[出售]所有所选资源, 你获得 1[分数]"

            },
        ]
    },
    {
        "id": 5,
        "name": "锡人",
        "enterprise": False,
        "camp": "dafault",
        "describe": "#",
        "skill": [
            {
                "type": "策略",
                "name": "建立威信",
                "describe": "获得 1[分数]。"
                            "支付 12[货币] -> 获得 1[至纯源石]。"
                            "支付 15[货币] -> 获得 1[至纯源石]。"
            },
            {
                "type": "计谋",
                "name": "深谋远虑",
                "describe": "将你的角色牌棋牌区中的牌收回手牌, 每收回一张, 获得 5[货币]或[移动影响力]"

            },
        ]
    },
    {
        "id": 6,
        "name": "玛恩纳",
        "enterprise": True,
        "camp": "dafault",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 7,
        "name": "山",
        "enterprise": True,
        "camp": "dafault",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 8,
        "name": "森蚺",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 9,
        "name": "异客",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 10,
        "name": "多萝西",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 11,
        "name": "泥岩",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 12,
        "name": "可露希尔",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 13,
        "name": "W",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 14,
        "name": "银灰",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
    {
        "id": 15,
        "name": "凯尔希",
        "enterprise": True,
        "camp": "RHODES_ISLAND",
        "describe": "#",
        "strategy": {},
        "scheme": {}
    },
]
# 标准版只有这五个角色
STANDARD = [1, 2, 3, 4, 5]
