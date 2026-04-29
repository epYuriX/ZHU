# game / round
class Round:
    """
    回合类
    """

    def __init__(self, order: list[str], banker: str):
        """
        # 初始化
        :param order: 行动顺序
        :param banker: 当前回合庄家
        """
        # 数据初始化
        self.order = order
        self.banker = banker
        self.cycles = 2
        self.turn_index = 0
        
