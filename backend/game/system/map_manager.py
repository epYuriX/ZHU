# game/system/map_manager.py
from game.entity.map import *


class MapManager:
    """
    地图控制器
        nodes[]: 节点信息
            id: 节点 id
            type: 节点类型 node - 资源点, link - 通道
            lv: 节点等级
            name: 节点名
            area: 所属区块
            color: 所属区颜色
            resource: # 资源类型
            resource_c: # 资源乘数
            parking: # 存在玩家所属方
            inf_c: # 影响力棋子容量
            inf_1: # 影响力1所属方
            inf_2: # 影响力2所属方
        links[]: 链路信息
        map{}: 完整地图
    方法列表
        __init__(): 初始化
        update(): 更新地图
        ---------------- 影响力相关
        put_inf(): 放置影响力
        del_inf(): 移除影响力
        move_inf(): 移动影响力
        replace_inf(): 替换影响力
        del_other_inf(): 移除其他势力的影响力
        ---------------- 移动城市相关
        put_player(): 放置移动城市
        del_inf(): 移除移动城市
        move_inf(): 移动移动城市
        ---------------- 节点相关
        set_node_type(): 设置资源点类型
        adjacent_nodes(): 获取相邻节点列表
        adjacent_resource(): 获取相邻资源点列表
    """

    def __init__(self):
        """
        初始化
        """
        self.nodes = NODE_DATAILS_4
        self.links = ADJACENCY_LIST_4
        self.map = MAP_4

    def update(self):
        """
        更新地图
        """
        self.links = ADJACENCY_LIST_APPEND_4
        self.map = MAP_APPEND_4

    def put_inf(self, nid, ident) -> bool:
        """
        放置影响力
        :param nid: 节点 id
        :param ident: 玩家身份
        :return: 是否成功放置
        """
        node = self.nodes[nid]
        if node.inf_1 == "null":
            node.inf_1 = ident
            return True
        elif node.int_c > 1 and node.inf_2 == "null":
            node.inf_2 = ident
            return True
        return False

    def del_inf(self, nid, ident) -> bool:
        """
        移除影响力
        :param nid:
        :param ident:
        :return:
        """
        node = self.nodes[nid]
        if node.inf_1 == ident:
            node.inf_1 = "null"
            return True
        elif node.inf_c > 1 and node.inf_2 == ident:
            node.inf_2 = "null"
            return True
        return False

    def move_inf(self, ident, nid, nid_new) -> bool:
        """
        移动影响力
        :param ident:
        :param nid:
        :param nid_new:
        :return:
        """
        if self.del_inf(nid, ident):
            if self.put_inf(nid_new, ident):
                return True
        return False

    def replace_inf(self, nid: int, ident: str, ident_new: str) -> bool:
        """
        替换影响力
        :param nid:
        :param ident:
        :param ident_new:
        :return:
        """
        node = self.nodes[nid]
        if node.inf_1 == ident:
            node.inf_1 = ident_new
            return True
        elif node_c > 1 and node.inf_2 == ident:
            node.inf_2 = ident_new
            return True
        return False

    def del_other_inf(self, nid, ident):
        """
        移除其他势力的影响力
        :param nid:
        :param ident:
        :return:
        """
        node = self.nodes[nid]
        if node.inf_1 != ident:
            node.inf_1 = "null"
        if node.inf_c > 1 and node.inf_2 != ident:
            node.inf_2 = "null"

    def put_player(self, nid, ident) -> bool:
        """
        放置玩家角色
        :param nid:
        :param ident:
        :return:
        """
        node = self.nodes[nid]
        if node.type != "node":
            return False
        if node.parking != "null":
            return False
        node.parking = ident
        return True

    def del_player(self, nid, ident) -> bool:
        """
        移除玩家角色
        :param nid:
        :param ident:
        :return:
        """
        node = self.nodes[nid]
        if node.type != "node":
            return False
        if node.parking != ident:
            return False
        node.parking = "null"
        return True

    def move_player(self, ident, nid, by, nid_new) -> bool:
        """
        移动玩家角色
        :param ident:
        :param nid:
        :param by: 经过的路径
        :param nid_new:
        :return:
        """
        link = next((i for i in self.links[nid] if i['id'] == nid_new and i['by'] == by), False)
        if link:
            if self.del_player(nid, ident):
                if self.put_player(nid_new, ident):
                    self.del_other_inf(link.id, ident)
                    self.del_other_inf(link.by, ident)
                    self.put_inf(nid, ident)
                    return True
        return False

    def set_node_type(self, nid, res, res_c) -> bool:
        """
        设置节点的资源类型
        :param nid:
        :param res:
        :param res_c:
        :return:
        """
        node = self.nodes[nid]
        if node.type != "node":
            return False
        if node.resource != "null":
            return False
        node.resource = res
        node.resource_c = res_c
        return True

    def adjacent_nodes(self, nid) -> list:
        """
        相邻节点
        :param nid:
        :return:
        """
        return self.map[nid]

    def adjacent_resource(self, nid):
        """
        相邻资源点
        :param nid:
        :return:
        """
        node = self.nodes[nid]
        if node.type != "node":
            return False
        return list({i["id"] for i in self.links[nid]})
