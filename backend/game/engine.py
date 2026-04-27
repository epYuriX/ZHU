# game / engine.py
import random
from .map import MapManager
from .player import Player


class GameEngine:
    def __init__(self, user_ids: list):
        # 随机分配顺序
        random.shuffle(user_ids)
        self.player_order = user_ids
        self.players = {
            uid: Player(uid, f"P{i + 1}") for i, uid in enumerate(user_ids)
        }
        # 设 P1 为初始庄家
        self.banker_id = user_ids[0]
        self.player_ids = user_ids
        # 玩家行动顺序管理
        self.active_order = []  # 本回合行动顺序
        self.turn_index = 0  # 回合内玩家指针

        self.phase = "setup"
        self.current_round = 0  # 回合数

    def prepare_new_round(self):
        """
        回合开始时根据当前庄家设置本回合行动顺序
        :return:
        """
        self.current_round += 1
        idx = self.player_ids.index(self.banker_id)
        self.active_order = self.player_ids[idx:] + self.player_ids[:idx]
        self.turn_index = 0

    def get_current_user_id(self):
        return self.active_order[self.turn_index]

    def set_next_banker_manually(self, user_id: int):
        """
        设定下回合庄家
        :param user_id:
        :return:
        """
        self.banker_id = user_id
