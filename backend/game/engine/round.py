# game / engine / round.py
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

    def player_action(self, ident):
        """
        玩家行动
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
