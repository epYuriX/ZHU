# game / engine.py
import random
from .map_manager import MapManager
from .resource_manager import ResourceManager
from .player import Player


class GameEngine:
    """
    游戏控制器
        phase: 当前阶段
        current_round: 当前回合数
        ---------------- 玩家管理
        players: {identity: Player对象} 玩家实体 (P1-P4)
        uid_to_ident: {user_id: identity} 映射表
        player_identities: 玩家座位表 ["P1", "P2", "P3", "P4"]
        active_order: 当前回合操作顺序
        turn_index: 当前在该顺序下行动指针 (0-3)
        ---------------- 庄家机制
        current_banker: 本回合庄家身份
        next_banker: 预设下回合庄家身份
    """

    def __init__(self, user_ids: list):
        self.map_manager = MapManager()
        self.resource_manager = ResourceManager()

        # 初始化身份映射与玩家实体
        random.shuffle(user_ids)
        self.uid_to_ident = {uid: f"P{i + 1}" for i, uid in enumerate(user_ids)}
        self.player_identities = [f"P{i + 1}" for i in range(len(user_ids))]
        self.players: Dict[int, Player] = {
            f"P{i + 1}": Player(uid, f"P{i + 1}") for i, uid in enumerate(user_ids)
        }

        # 庄家初始化
        self.current_banker = self.player_identities[0]
        self.next_banker = self.player_identities[1] if len(self.player_identities) > 1 else self.current_banker

        # 流程初始化
        self.phase = "prep"
        self.current_round = 0
        self.active_order = []
        self.turn_index = 0

    def get_game_state(self):
        """获取游戏快照"""
        return {
            "info": {
                "phase": self.phase,
                "round": self.current_round,
                "banker": self.current_banker,
                "next_banker": self.next_banker,
                "active_user": self._get_current_active_user()  # 返回的是P1-P4
            },
            "players": {
                ident: {
                    "identity": p.identity,
                    "pos": p.current_node,
                    "res": {
                        "money": p.money,
                        "yuan_yan": p.yuan_yan,
                        "yuan_shi": p.yuan_shi,
                        "yi_tie": p.yi_tie,
                        "zcys": p.zcys
                    },
                    "is_banker": p.is_banker
                } for ident, p in self.players.items()
            }
        }

    def start_new_round(self):
        """进入新回合"""
        self.current_round += 1
        idx = self.player_identities.index(self.current_banker)
        default_next_idx = (idx + 1) % len(self.player_identities)
        self.next_banker = self.player_identities[default_next_idx]

        for ident, p in self.players.items():
            p.is_banker = (ident == self.current_banker)

        self.active_order = self.player_identities[idx:] + self.player_identities[:idx]
        self.turn_index = 0

    def finish_round(self):
        """
        回合结束
        """
        self.current_banker = self.next_banker
        self.start_new_round()

    async def handle_prep_select(self, user_id: int, node_id: int):
        """
        初始选位
        """
        ident = self.uid_to_ident.get(user_id)
        if not ident:
            return {"status": "error", "msg": "非法用户"}
        if self.phase != "prep":
            return {"status": "error", "msg": "非准备阶段"}
        if ident != self.player_identities[self.turn_index]:
            return {"status": "error", "msg": "请等待其他玩家选位"}
        node = self.map_manager.get_node_info(node_id)
        if not node or node["id"] not in self.map_manager.initial_optional_ids:
            return {"status": "error", "msg": "不可选择该位置作为起点"}
        if node["parking"] != "null":
            return {"status": "error", "msg": "该位置已被占领"}

        # 占领
        player = self.players[ident]
        player.current_node = node_id
        node["parking"] = ident

        # 放置初始影响力
        self._place_influence(ident, node_id)

        discovery_result = await self._discover_resource_node(ident, node_id)
        self.turn_index += 1

        if self.turn_index >= len(self.player_identities):
            self.phase = "playing"
            self.start_new_round()
            return {"status": "success", "msg": "游戏开始", "discovery": discovery_result, "next_phase": "playing"}

        return {"status": "success", "msg": "选位成功", "discovery": discovery_result}

    def _get_current_active_user(self):
        order = self.player_identities if self.phase == "prep" else self.active_order
        return order[self.turn_index] if self.turn_index < len(order) else None

    async def _discover_resource_node(self, ident: str, node_id: int):
        player = self.players.get(ident)
        node = self.map_manager.get_node_info(node_id)
        if node.get("resource") != "null": return None

        level = f"lv{node['lv']}"
        card = self.resource_manager.draw_resource_card(level)
        if not card: return None

        node["resource"] = card["map_attribute"]["resource"]
        node["resource_c"] = int(card["map_attribute"]["resource_c"])

        event_data = {
            "node_id": node_id,
            "card_name": card["name"],
            "describe": card["describe"],
            "options": card["instant_options"],
        }
        player.pending_event = event_data
        return event_data

    # --- 影响力核心逻辑 (统一使用 ident) ---

    def _place_influence(self, ident: str, node_id: int):
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == "null":
            node["inf_1"] = ident
            return True
        elif node["inf_c"] >= 2 and node["inf_2"] == "null":
            node["inf_2"] = ident
            return True
        return False

    def _remove_influence(self, node_id: int, target_ident: str):
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == target_ident:
            node["inf_1"] = "null"
            return True
        elif node["inf_2"] == target_ident:
            node["inf_2"] = "null"
            return True
        return False

    def _replace_influence(self, attacker_ident: str, node_id: int, defender_ident: str):
        if self._remove_influence(node_id, defender_ident):
            return self._place_influence(attacker_ident, node_id)
        return False

    def _move_influence(self, ident: str, from_node_id: int, to_node_id: int):
        if self._place_influence(ident, to_node_id):
            self._remove_influence(from_node_id, ident)
            return True
        return False

    def skill_steal_banker(self, thief_ident: str):
        self.next_banker = thief_ident