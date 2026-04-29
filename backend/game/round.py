# game / round
class Round:
    """
    回合类
        order[]: 行动顺序
        cycles = 2: 总轮数 2
        current_cycle: 当前是第几轮
        turn_index: 行动玩家指针
        finished: 是否所有玩家行动结束
    // 回合说明
        1. 角色牌盖放
        2. 玩家行动 (2轮)
            主要行动 (6选1)
                部署: [放置影响力]
                调度: [移动自己的一个影响力] * 2
                探索: 支付路费, 结算事件, 在目标资源点放置一个影响力
                城市移动: 支付[源石] * 3, 移动玩家至相邻资源点
                建设: 支付费用, 放置设施牌, 结算分数, 结算设施牌入场效果
                特殊行动: 使用已宣告的城市样式牌所解锁的特殊行动
            快速行动 (主要行动前后，任意次数)
                使用角色牌: 翻开自己盖放的角色牌, 选择牌上的效果发动
                宣告城市样式: 用已建设的设施满足宣告条件, 每个设施只能用 1 次
        3. 采集资源
        4. 收尾
    """

    def __init__(self, order: list[str]):
        """
        # 初始化
        :param order: 行动顺序
        :param banker: 当前回合庄家
        """
        # 数据初始化
        self.order = order
        self.current_cycle = 1
        self.cycles = 2
        self.turn_index = 0
        self.finished = False
        print("--- * 回合开始 * ---")
        print("本回合行动顺序为：")
        for i in order:
            print(i, end=" ")

    def get_current_player(self):
        """
        获取当前行动玩家
        :return:
        """
        if self.finished:
            return None
        return self.order[self.turn_index]

    def next_turn(self):
        """
        回合推进
        """
        self.turn_index += 1
        if self.turn_index >= len(self.order):
            self.turn_index = 0
            self.current_cycle += 1
            if self.current_cycle > self.cycles:
                self.finished = True

    def on_round_start(self):
        """
        回合开始时
        """
        pass

    def on_round_end(self):
        """
        回合结束
        """
        # 收资源
        pass

    def on_turn_start(self, ident):
        """
        某个玩家开始行动
        :param ident:
        """
        pass

    def on_turn_end(self, ident):
        """
        某个玩家结束行动
        :param ident:
        """
        pass

    def select_member(self):
        """
        角色牌盖放
        :return:
        """
        pass

    def collect_resources(self):
        """
        采集资源
        :return:
        """
        pass
