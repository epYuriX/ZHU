# game / engine.py
import random
from .map import MapManager as MapManager
from .player import Player


class GameEngine:
    def __init__(self, user_ids: list):
        """
        游戏准备
        :param user_ids:
        """
        self.map_manager = MapManager()
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
        # 游戏开始时其他操作
        #
        #
        #
        #
        #

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
        # 回合结束时其它操作
        #
        #
        #
        #
        #
        # 下一回合开始
        self.start_new_round()

    async def handle_setup_select(self, user_id: int, node_id: int):
        """
        初始选位
        :param user_id:
        :param node_id:
        :return:
        """
        # 校验
        if self.phase != "setup":
            return {
                "status": "error",
                "msg": "当前不是选位阶段"
            }
        if user_id != self.player_order[self.turn_index]:
            return {
                "status": "error",
                "msg": "请等待其他玩家选位"
            }
        # 节点校验
        node = self.map_manager.get_node_info(node_id)
        if not node or node["id"] not in self.map_manager.initial_optional_ids:
            return {
                "status": "error",
                "msg": "不可选择该位置作为起点"
            }
        if node["parking"] != "null":
            return {
                "status": "error",
                "msg": "不可选择已有玩家的位置作为起点"
            }
        # 占领
        player = self.players[user_id]
        player.current_node = node_id
        node["parking"] = player.identity
        self.turn_index += 1
        #
        if self.turn_index >= len(self.player_ids):
            self.phase = "playing"
            self.start_new_round()
            return {
                "status": "success",
                "msg": "选位结束, 游戏开始",
                "next_phase": "playing"
            }
        return {
            "status": "success",
            "msg": "选位成功",
            "next_player": self.player_order[self.turn_index]
        }

    def skill_steal_banker(self, thief_id: int):
        """
        切换 banker
        :param thief_id:
        :return:
        """
        self.next_banker = thief_id
