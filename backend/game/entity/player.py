# game/entity/player.py
class Player:
    """
    游戏内玩家类
        identity: 玩家在局内编号 (P1, P2, P3, P4)
        uid: 玩家账号 id
        score: 得分
        character: 人物
        resources: 资源
            money: 钱币
            yuan_yan: 源岩
            yuan_shi: 源石
            yi_tie: 异铁
            zcys: 至纯源石
        role: 角色
            cover: 盖放
            available[]: 可用
            discard[]: 弃牌区
        current_node: 在地图上的位置
        is_banker: 本回合是否为庄家



        space: 每个玩家有一个 3 * 3 的建筑区用于摆放建筑卡

        pending_event: 待处理事件
    """

    def __init__(self, uid, identity):
        self.identity = identity  # P1, P2, P3, P4
        self.uid = uid
        self.character = None
        self.score = 0
        self.resources = {
            "money": 0,
            "yuan_yan": 0,
            "yuan_shi": 0,
            "yi_tie": 0,
            "zcys": 0,
        }
        self.role = {
            "cover": None,
            "available": [],
            "discard": [],
        }
        self.space = [
            ["null", "null", "null"],
            ["null", "null", "null"],
            ["null", "null", "null"],
        ]
        self.current_node = None
        self.is_banker = False
        self.pending_event = None
