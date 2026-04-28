# game / engine.py
import random
from .map_manager import MapManager
from .resource_manager import ResourceManager
from .player import Player


class GameEngine:
    """
    游戏控制器
        phase: 当前阶段 (prep / playing)
        current_round: 当前回合数
        ---------------- 玩家管理
        players: {ident: Player对象} 玩家实体 (Key 为 P1-P4)
        player_identities: 座位表 ["P1", "P2", "P3", "P4"]
        uid_to_ident: 用户ID到身份的映射表 (仅用于初始化和外部查询)
        active_order: 当前回合操作顺序 (身份标识列表)
        turn_index: 当前在该顺序下行动指针
        ---------------- 庄家机制
        current_banker: 本回合庄家身份 (ident)
        next_banker: 预设下回合庄家身份 (ident)
    """

    def __init__(self, user_ids: list):
        """
        游戏初始化
        :param user_ids: 外部传入的原始用户ID列表
        """
        self.map_manager = MapManager()
        self.resource_manager = ResourceManager()

        # 1. 游戏启动瞬间，完成身份锚定
        random.shuffle(user_ids)
        self.player_identities = [f"P{i + 1}" for i in range(len(user_ids))]
        self.uid_to_ident = {uid: f"P{i + 1}" for i, uid in enumerate(user_ids)}

        # 2. 初始化玩家实体 (内部逻辑只通过 ident 寻找 Player)
        self.players = {
            ident: Player(self._get_uid_by_ident(ident), ident)
            for ident in self.player_identities
        }

        # 3. 庄家初始化 (使用身份标识)
        self.current_banker = self.player_identities[0]
        self.next_banker = self.player_identities[1] if len(user_ids) > 1 else self.player_identities[0]

        # 4. 流程初始化
        self.phase = "prep"
        self.current_round = 0
        self.active_order = []
        self.turn_index = 0

    def _get_uid_by_ident(self, ident: str):
        """内部工具：由身份获取原始UID"""
        for uid, i in self.uid_to_ident.items():
            if i == ident:
                return uid
        return None

    def get_game_state(self):
        """
        获取游戏快照 (对外展示时也统一使用 ident)
        """
        return {
            "info": {
                "phase": self.phase,
                "round": self.current_round,
                "banker": self.current_banker,
                "next_banker": self.next_banker,
                "active_user": self._get_current_active_ident()
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
                        "zcys": p.zcys,
                        "score": p.score,
                    },
                    "is_banker": p.is_banker
                } for ident, p in self.players.items()
            }
        }

    def start_new_round(self):
        """
        进入新回合
        :return:
        """
        self.current_round += 1
        # 庄家顺位逻辑 (基于身份列表)
        idx = self.player_identities.index(self.current_banker)
        default_next_idx = (idx + 1) % len(self.player_identities)
        self.next_banker = self.player_identities[default_next_idx]

        for ident, p in self.players.items():
            p.is_banker = (ident == self.current_banker)

        # 生成本回合行动顺序 (身份列表)
        self.active_order = self.player_identities[idx:] + self.player_identities[:idx]
        self.turn_index = 0
        # 回合开始时其他操作
        #
        #
        #
        #

    def finish_round(self):
        """
        回合结束
        :return:
        """
        # 庄家转正
        self.current_banker = self.next_banker
        # 回合结束时其它操作
        #
        #
        #
        #
        # 下一回合开始
        self.start_new_round()

    async def handle_prep_select(self, ident: str, node_id: int):
        """
        初始选位
        :param ident: 玩家身份 (P1-P4)
        :param node_id:
        :return:
        """
        # 校验
        if self.phase != "prep":
            return {
                "status": "error",
                "msg": "非准备阶段"
            }
        if ident != self.player_identities[self.turn_index]:
            return {
                "status": "error",
                "msg": f"当前应由 {self.player_identities[self.turn_index]} 选位"
            }
        # 节点校验
        node = self.map_manager.get_node_info(node_id)
        if not node or node["id"] not in self.map_manager.initial_optional_ids:
            return {"status": "error", "msg": "不可选择该位置作为起点"}
        if node["parking"] != "null":
            return {"status": "error", "msg": "不可选择已有玩家的位置作为起点"}
        player = self.players[ident]
        player.current_node = node_id
        node["parking"] = ident

        # 放置初始影响力
        self._place_influence(ident, node_id)

        # 探索资源
        discovery_result = await self._discover_resource_node(ident, node_id)
        self.turn_index += 1

        # 5. 检查是否选位完毕
        if self.turn_index >= len(self.player_identities):
            self.phase = "playing"
            self.start_new_round()
            return {
                "status": "success",
                "msg": "选位结束, 游戏开始",
                "discovery": discovery_result,
                "next_phase": "playing"
            }

        card_name = discovery_result.get("card_name", "未知资源") if discovery_result else "未知资源"
        return {
            "status": "success",
            "msg": f"身份 {ident} 选位成功，发现了: {card_name}",
            "discovery": discovery_result,
            "next_player": self.player_identities[self.turn_index]
        }

    def _get_current_active_ident(self):
        """
        确定当前行动玩家身份
        :return:
        """
        order = self.player_identities if self.phase == "prep" else self.active_order
        return order[self.turn_index] if self.turn_index < len(order) else None

    # --- 底层私有方法：全参数 ident 化 ---

    async def _discover_resource_node(self, ident: str, node_id: int):
        """
        探索资源点
        :param ident:
        :param node_id:
        :return:
        """
        player = self.players.get(ident)
        node = self.map_manager.get_node_info(node_id)
        if node.get("resource") != "null":
            return None

        level = f"lv{node['lv']}"
        card = self.resource_manager.draw_resource_card(level)
        if not card:
            return None

        # 设置资源点类型
        node["resource"] = card["map_attribute"]["resource"]
        node["resource_c"] = card["map_attribute"]["resource_c"]

        event_data = {
            "node_id": node_id,
            "card_name": card["name"],
            "describe": card["describe"],
            "options": card["instant_options"],
        }
        player.pending_event = event_data
        return event_data

    def _place_influence(self, ident: str, node_id: int):
        """
        在指定地点放置影响力
        """
        player = self.players.get(ident)
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == "null":
            node["inf_1"] = player.identity
            return True
        elif node["inf_c"] >= 2 and node["inf_2"] == "null":
            node["inf_2"] = player.identity
            return True
        return False

    def _remove_influence(self, node_id: int, target_ident: str):
        """
        移除影响力
        :param target_ident: 目标身份字符串
        """
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == target_ident:
            node["inf_1"] = "null"
            return True
        elif node["inf_2"] == target_ident:
            node["inf_2"] = "null"
            return True
        return False

    def _replace_influence(self, attacker_ident: str, node_id: int, defender_ident: str):
        """
        替换影响力
        """
        if self._remove_influence(node_id, defender_ident):
            return self._place_influence(attacker_ident, node_id)
        return False

    def _move_influence(self, ident: str, from_node_id: int, to_node_id: int):
        """
        移动影响力
        """
        if self._place_influence(ident, to_node_id):
            self._remove_influence(from_node_id, ident)
            return True
        return False

    def skill_steal_banker(self, thief_ident: str):
        """
        切换下回合庄家身份
        """
        self.next_banker = thief_ident
