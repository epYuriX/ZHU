# managers/room_manager.py

from room.room import Room


class RoomManager:
    """
    房间管理器
    rooms{}:
        房间列表
        rid -> Room
    user_room_map{}:
        用户-房间映射
        uid -> rid
    next_rid:
        房间id自增
    """

    def __init__(self):
        """
        初始化
        """
        self.rooms = {}
        self.user_room_map = {}
        self.next_rid = 1000

    def create_room(self, oid: int):
        """
        创建房间
        :param oid: 房主id
        :return: Room / None
        """
        if oid in self.user_room_map:
            # 玩家已经在房间中
            return None
        self.next_rid += 1  # 房间id自增
        # 创建房间
        room = Room(rid=self.next_rid, oid=oid)
        self.rooms[room.rid] = room
        self.user_room_map[oid] = room.rid
        return room

    def join_room(self, uid: int, rid: int):
        """
        加入房间
        :param uid: 用户id
        :param rid: 房间id
        :return: bool
        """
        if uid in self.user_room_map:
            # 用户已经在房间中
            return False
        room = self.rooms.get(rid)
        if not room:
            # 房间不存在
            return False
        if room.player_cnt >= room.max_players:
            # 房间满员
            return False
        if room.status != "waiting":
            # 房间不是等待状态
            return False
        for seat, player in room.players.items():
            # 寻找空座位
            if player is None:
                room.players[seat] = uid
                room.player_cnt += 1
                self.user_room_map[uid] = rid
                return True
        return False

    def leave_room(self, uid: int):
        """
        离开房间
        :param uid: 用户id
        :return:
        """
        # 获取房间id
        rid = self.user_room_map.get(uid)
        if not rid:
            return
        # 获取房间
        room = self.rooms.get(rid)
        if not room:
            return
        # 房主退出 -> 解散房间
        if uid == room.oid:
            self.dissolve_room(rid)
            return
        # 删除玩家
        for seat, player in room.players.items():
            if player == uid:
                room.players[seat] = None
                break
        # 玩家数量减少
        if room.player_cnt > 0:
            room.player_cnt -= 1
        # 删除映射
        if uid in self.user_room_map:
            del self.user_room_map[uid]

        # 房间没人 -> 删除房间
        if room.player_cnt == 0:
            del self.rooms[rid]

    def dissolve_room(self, rid: int):
        """
        解散房间

        :param rid: 房间id
        :return:
        """
        room = self.rooms.get(rid)
        if not room:
            return
        # 删除所有玩家映射
        for uid in room.players.values():
            if uid is not None:
                if uid in self.user_room_map:
                    del self.user_room_map[uid]
        # 删除房间
        del self.rooms[rid]

        pass

    def get_room_list(self):
        """
        获取房间列表

        :return: list
        """

        result = []

        for room in self.rooms.values():
            result.append({

                "rid": room.rid,

                "oid": room.oid,

                "players": room.players,

                "player_cnt": room.player_cnt,

                "max_players": room.max_players,

                "status": room.status
            })

        return result

    def get_room_by_uid(self, uid: int):
        """
        通过uid获取房间

        :param uid: 用户id
        :return: Room / None
        """

        rid = self.user_room_map.get(uid)

        if not rid:
            return None

        return self.rooms.get(rid)


# 全局房间管理器
room_manager = RoomManager()
