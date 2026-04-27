# game / engine.py
import random
from .map import MapManager
from .player import Player


class GameEngine:
    def __init__(self, user_ids: list):
        """
        游戏准备
        :param user_ids:
        """
        # 随机分配顺序
        random.shuffle(user_ids)
        self.player_order = user_ids
        self.players = {
            uid: Player(uid, f"P{i + 1}") for i, uid in enumerate(user_ids)
        }
        # 设 P1 为初始庄家
        self.current_banker = user_ids[0]
        self.next_banker = user_ids[1]
        self.player_ids = user_ids
        # 玩家行动顺序管理
        self.active_order = []  # 本回合行动顺序
        self.turn_index = 0  # 回合内玩家指针

        self.phase = "setup"
        self.current_round = 0  # 回合数

    def start_new_round(self):
        """
        回合开始
        :return:
        """
        # 回合数 + 1
        self.current_round += 1
        # 预设下一位庄家
        idx = self.player_ids.index(self.current_banker)
        default_next_idx = (idx + 1) % len(self.player_ids)
        self.next_banker = self.player_ids[default_next_idx]
        # 生成本回合行动顺序
        self.active_order = self.player_ids[idx:] + self.player_ids[:idx];
        self.turn_index = 0
        # 回合开始时其他操作
        #
        #
        #
        #
        #

    def finish_round(self):
        """
        回合结束
        :return:
        """
        self.current_banker = self.next_banker
        # 回合结束操作
        #
        #
        #
        #
        #
        # 下一回合开始
        self.start_new_round()

    def skill_steal_banker(self, thief_id: int):
        """
        切换 banker
        :param thief_id:
        :return:
        """
        self.next_banker = thief_id
