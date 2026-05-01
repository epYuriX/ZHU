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
        facility: 设施
        city: 城市
        current_node: 在地图上的位置
        is_banker: 本回合是否为庄家

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
        self.facility = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.city = {}
        self.current_node = None
        self.is_banker = False

    def get_state(self):
        """
        获取玩家的完整状态
        :return:
            人物
            分数
            资源
            角色
            设施
            城市样式
            是否为庄家
        """
        return {
            "character": self.character,
            "score": self.score,
            "resources": self.resources,
            "role": self.role,
            "facility": self.facility,
            "city": self.city,
            "is_banker": self.is_banker
        }

    def add_resource(self, res, amount):
        """
        增加资源
        :param res:
        :param amount:
        """
        if res in self.resources:
            self.resources[res] += amount

    def sub_resource(self, res, amount):
        """
        减少资源
        :param res:
        :param amount:
        """
        if res in self.resources and self.resources[res] >= amount:
            self.resources[res] -= amount
