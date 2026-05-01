# game / map_manager.py
from platform import node

from game.data.map_config import (
    NODE_DATAILS_4,
    ADJACENCY_LIST_4,
    ADJACENCY_LIST_APPEND_4,
    OPTIONAL_4
)


class MapManager:
    """
    地图管理器
    """

    def __init__(self):
        self.nodes = {
            node["id"]: node for node in NODE_DATAILS_4
        }
        self.base_adj = ADJACENCY_LIST_4
        self.full_adj = ADJACENCY_LIST_APPEND_4
        self.initial_optional_ids = OPTIONAL_4

    def get_node_info(self, node_id: int):
        """
        获取节点信息
        :param node_id:
        :return:
        """
        return self.nodes.get(node_id)

    def get_setup_options(self):
        """
        获取可选点列表
        :return:
        """
        options = []
        for n_id in self.initial_optional_ids:
            node = self.get_node_info(n_id)
            if node and node.get("parking") == "null":
                options.append(node)
        return options

    def update_node_oarking(self, node_id: int, player_identity: str):
        """
        更新节点占领状态
        :param node_id:
        :param player_identity:
        :return:
        """
        if node_id in self.nodes:
            self.nodes[node_id]["parking"] = player_identity
            return True
        return False

    def get_movable_nodes(self, current_node_id: int, current_round: int):
        """
        可移动列表
        :param current_node_id:
        :param current_round:
        :return:
        """
        active_list = self.full_adj if current_round >= 4 else self.base_adj
        if 0 < current_node_id < len(active_list):
            return active_list[current_node_id]
        return []

    def is_move_valid(self, start_id: int, end_id: int, current_round: int) -> bool:
        """
        移动校验
        :param start_id:
        :param end_id:
        :param current_round:
        :return:
        """
        movable = self.get_movable_nodes(start_id, current_round)
        return any(item["id"] == end_id for item in movable)
