# game/engine/game_engine.py
import random

from game.system import MapManager
from game.event import EventManager
from game.action import ActionManager
from game.entity import Player


class GameEngine:
    """
    游戏控制核心
        ---------------- 对局信息
        phase: 游戏状态 prep: 准备中,
        current_round: 当前回合数: 0: 游戏开始时, 1~8, 9: 最终结算
        current_banker: 当前回合庄家
        next_banker: 下回合庄家
        ---------------- 玩家信息

        facility: 设施
        city: 城市样式
        ---------------- 控制类
        map_manager: 地图控制
        event_manager: 事件(地图探索抽取资源卡)
        action_manager: 玩家操作
    """

    def __init__(self, user_ids: list):
        # 初始化
        self.map_manager = MapManager()
        self.event_manager = EventManager()
        self.action_manager = ActionManager()
        # 初始化
        # 玩家
        random.shuffle(user_ids)
        self.player_identities = [f"P{i + 1}" for i in range(len(user_ids))]
        self.uid_to_ident = {
            uid: ident for uid, ident in zip(user_ids, self.player_identities)
        }
        self.players = {
            ident: Player(self._get_uid_by_ident(ident), ident)
            for ident in self.player_identities
        }
        self.character = {
            "P1": {},
            "P2": {},
            "P3": {},
            "P4": {},
        }

        self.role = {
            "P1": {
                "cover": None,
                "available": [],
                "discard": [],
            },
            "P2": {
                "cover": None,
                "available": [],
                "discard": [],
            },
            "P3": {
                "cover": None,
                "available": [],
                "discard": [],
            },
            "P4": {
                "cover": None,
                "available": [],
                "discard": [],
            },
        }
        self.facility = {
            "P1": {},
            "P2": {},
            "P3": {},
            "P4": {},
        }
        self.city = {
            "P1": {},
            "P2": {},
            "P3": {},
            "P4": {},
        }
        # 游戏状态
        self.phase = "prep"
        self.current_round = 0
        # 庄家
        self.current_banker = self.player_identities[0]
        self.next_banker = self.player_identities[1]
        # 回合 / 行动
        self.round: Round | None = None
        self.current_action_session: ActionSession | None = None

    def _get_uid_by_ident(self, ident: str):
        for uid, i in self.uid_to_ident.items():
            if i == ident:
                return uid
        return None

    def game_prep(self):
        """
        游戏准备阶段
        """
        # 接下来要在这里制作玩家选择位置

    def start_new_round(self):
        self.current_round += 1
