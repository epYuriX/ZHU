# game / player.py
class Player:
    """
    游戏内玩家类
        user_id: 玩家账号 id
        identity: 玩家在局内编号 (P1, P2, P3, P4)
        score: 得分
        current_node: 在地图上的位置
        is_banker: 本回合是否为庄家
        ---------------- 货币 / 资源
        money: 钱币
        yuan_yan: 源岩
        yuan_shi: 源石
        yi_tie: 异铁
        zcys: 至纯源石
        ---------------- 干员 / 本回合出场干员
        member_list: 干员列表
        member: 本回合出场干员
        ---------------- 建筑区
        space: 每个玩家有一个 3 * 3 的建筑区用于摆放建筑卡
    """

    def __init__(self, user_id, identity):
        self.user_id = user_id
        self.identity = identity  # P1, P2, P3, P4
        self.score = 0
        self.money = 0
        self.yuan_yan = 0
        self.yuan_shi = 0
        self.yi_tie = 0
        self.zcys = 0
        self.member_list = []
        self.member = None
        self.space = [
            ["null", "null", "null"],
            ["null", "null", "null"],
            ["null", "null", "null"],
        ]
        self.current_node = None
        self.is_banker = False
