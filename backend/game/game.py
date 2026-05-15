# game/game.py
import random


class Game:
    """
    游戏类
        room: 所属房间
        turn_order: 玩家顺序
        turn_index: 当前回合数
    方法列表
        __init__(room): 初始化
        init_game(): 游戏初始化
    """

    def __init__(self, room):
        """
        初始化
        :param room:
        """
        self.room = room
        self.turn_order = []
        self.turn_index = 0
        self.init_game()

    def init_game(self):
        """
        游戏初始化
        :return:
        """
        # 随机座次
        players = []
        for uid in self.room.players.values():
            if uid is not None:
                players.append(uid)
        random.shuffle(players)
        self.turn_order = players
