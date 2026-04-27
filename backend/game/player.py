# game / player.py
class Player:
    def __init__(self, user_id, identity):
        self.user_id = user_id
        self.identity = identity  # P1, P2, P3, P4
        self.money = 0  # 钱
        self.yuan_yan = 0  # 源岩
        self.yuan_shi = 0  # 源石
        self.yi_tie = 0  # 异铁
        self.zcys = 0  # 至纯源石
        self.current_node = None  # 当前位置
