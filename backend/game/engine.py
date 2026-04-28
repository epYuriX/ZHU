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
        players: {user_id: Player对象} 玩家实体
        player_ids: 座位表
        player_order: 准备阶段操作顺序
        active_order: 当前回合操作顺序 (随庄家动态调整)
        trun_index: 当前在该顺序下行动指针 (0-3)
        ---------------- 庄家机制
        current_banker: 本回合庄家ID
        next_banker: 预设下回合庄家ID
    """

    def __init__(self, user_ids: list):
        """
        游戏初始化
        :param user_ids:
        """
        self.map_manager = MapManager()
        self.resource_manager = ResourceManager()
        # 分配顺序
        random.shuffle(user_ids)
        self.player_ids = user_ids
        self.player_order = user_ids
        self.players = {
            uid: Player(uid, f"P{i + 1}") for i, uid in enumerate(user_ids)
        }
        # 庄家初始化
        self.current_banker = user_ids[0]
        self.next_banker = user_ids[1]
        # 流程初始化
        self.phase = "prep"
        self.current_round = 0
        self.active_order = []  # 本回合行动顺序
        self.turn_index = 0  # 回合内玩家指针
        # 游戏开始时其他操作
        #
        #
        #
        #
        #

    def get_game_state(self):
        """
        获取游戏快照
        """
        return {
            "info": {
                "phase": self.phase,
                "round": self.current_round,
                "banker": self.current_banker,
                "next_banker": self.next_banker,
                "active_user": self._get_current_active_user()
            },
            "players": {
                uid: {
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
                } for uid, p in self.players.items()
            }
        }

    def start_new_round(self):
        """
        进入新回合
        :return:
        """
        self.current_round += 1
        # 庄家顺位
        idx = self.player_ids.index(self.current_banker)
        default_next_idx = (idx + 1) % len(self.player_ids)
        self.next_banker = self.player_ids[default_next_idx]
        for uid, p in self.players.items():
            p.is_banker = (uid == self.current_banker)
        # 生成本回合行动顺序
        self.active_order = self.player_ids[idx:] + self.player_ids[:idx]
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
        # 庄家转正
        self.current_banker = self.next_banker
        # 回合结束时其它操作
        #
        #
        #
        #
        #
        # 下一回合开始
        self.start_new_round()

    async def handle_prep_select(self, user_id: int, node_id: int):
        """
        初始选位
        :param user_id:
        :param node_id:
        :return:
        """
        # 校验
        if self.phase != "prep":
            return {
                "status": "error",
                "msg": "非准备阶段"
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
        discovery_result = await self._discover_resource_node(user_id, node_id)
        self.turn_index += 1
        #
        if self.turn_index >= len(self.player_ids):
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
            "msg": f"选位成功，你发现了: {card_name}",
            "discovery": discovery_result,
            "next_player": self.player_order[self.turn_index]
        }

    def _get_current_active_user(self):
        """
        确定当前行动玩家
        :return:
        """
        order = self.player_order if self.phase == "prep" else self.active_order
        return order[self.turn_index] if self.turn_index < len(order) else None

    async def _discover_resource_node(self, user_id: int, node_id: int):
        """
        探索资源点
        :param user_id:
        :param node_id:
        :return:
        """
        player = self.players.get(user_id)
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

    def _place_influence(self, user_id: int, node_id: int):
        """
        在指定地点放置影响力
        :return:
        """
        player = self.players.get(user_id)
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == "null":
            node["inf_1"] = player.identity
            return True
        elif node["inf_c"] >= 2 and node["inf_2"] == "null":
            node["inf_2"] = player.identity
            return True
        return False

    def _remove_influence(self, node_id: int, target_identity: str):
        """
        移除影响力
        :param node_id:
        :param target_identity:
        :return:
        """
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == target_identity:
            node["inf_1"] = "null"
            return True
        elif node["inf_2"] == target_identity:
            node["inf_2"] = "null"
            return True
        return False

    def _relace_influence(self, user_id: int, node_id: int, target_identity: str):
        """
        将节点上属于 target_identity 的影响力替换为 user_id 的
        :param user_id:
        :param node_id:
        :param target_identity:
        :return:
        """
        player = self.players.get(user_id)
        node = self.map_manager.get_node_info(node_id)
        if node["inf_1"] == target_identity:
            node["inf_1"] = player.identity
            return True
        elif node["inf_2"] == target_identity:
            node["inf_2"] = player.identity
            return True
        return False

    def _move_influence(self, user_id: int, from_node_id: int, to_node_id: int):
        """
        将自己的影响力从 A 点移到 B 点
        :param user_id:
        :param from_node_id:
        :param to_node_id:
        :return:
        """
        player = self.players[user_id]
        if self._place_influence(user_id, to_node_id):
            self._remove_influence(from_node_id, player.identity)
            return True
        return False

    def skill_steal_banker(self, thief_id: int):
        """
        切换 banker
        :param thief_id:
        :return:
        """
        self.next_banker = thief_id
