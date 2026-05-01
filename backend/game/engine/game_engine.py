# game/engine/game_engine.py
import random

from game.system import MapManager
from game.event import EventManager
from game.action import ActionManager
from game.entity import Player


class GameEngine:
    """
    游戏控制核心
        map_manager: 地图控制
        event_manager: 事件(地图探索抽取资源卡)
        action_manager: 玩家操作
    功能:
        1. 管理全局状态
        2. 初始化游戏系统
        3. 控制回合推进
        4. 接收玩家操作
        5. 调用 ActionManager
        6. 触发事件

    """

    def __init__(self, user_ids: list):
        # 初始化
        self.map_manager = MapManager()
        self.event_manager = EventManager()
        self.action_manager = ActionManager()
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

    def start_new_round(self):
        self.current_round += 1
        