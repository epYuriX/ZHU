# game/engine/round.py
class Round:
    """
    回合类
        order[]: 行动顺序
        cycles = 2: 总轮数 2
        current_cycle: 当前是第几轮
        turn_index: 行动玩家指针
        finished: 是否所有玩家行动结束
        phase: 阶段 start -> action -> end
    // 回合说明
        1. 角色牌盖放
        2. 玩家行动 (2轮)
        3. 采集资源
        4. 收尾
    """

    def __init__(self, engine, order: list[str]):
        """
        # 初始化
        :param engine: GameEngine 实例
        :param order: 行动顺序
        """
        # 数据初始化
        self.engine = engine
        self.order = order
        self.current_cycle = 1
        self.cycles = 2
        self.turn_index = 0
        self.finished = False
        self.phase = "start"

    def get_current_player(self):
        """
        获取当前行动玩家
        :return:
        """
        if self.finished:
            return None
        return self.order[self.turn_index]

    def start_phase(self):
        """
        回合开始时
        """
        # 回合开始时操作
        # 1. 盖放角色牌
        self.select_roles()
        self.phase = "action"
        pass

    def select_roles(self):
        """
        盖牌
        """
        for ident in self.order:
            player = self.engine.players.get(ident)
            if player:
                self.engine.action_manager.select_role(player)

    def next_turn(self):
        """
        回合推进
        """
        self.turn_index += 1
        if self.turn_index >= len(self.order):
            self.turn_index = 0
            self.current_cycle += 1
            if self.current_cycle > self.cycles:
                self.phase = "end"

    def end_phase(self):
        """
        回合结束
        """
        # 回合结束时操作
        # 其它回合结束时操作队列[]
        # 如确认下回合庄家等
        # 收资源
        #
        #
        #
        self.finished = True
        pass

    def player_action(self, ident):
        """
        玩家行动
        :param ident:
        """
        pass


