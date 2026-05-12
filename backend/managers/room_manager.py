# managers/room_manager.py
from room import Room


class RoomManager:
    """
    房间管理器
        rooms{}: 房间列表
        user_room_map{}: 用户-房间映射 (uid -> rid)
        next_rid: 房间id自增
    """

    def __init__(self):
        """
        初始化
        """
        self.rooms = {}  # rid -> Room
        self.user_room_map = {}  # uid -> rid
        self.next_rid = 1000  # 房间id自增

    def create_room(self, oid: int):
        """
        创建房间
        :param oid: 房主id
        :return: Room
        """
        if oid in self.user_room_map:
            # 该玩家已在房间中
            return None
        self.next_rid += 1
        room = Room(rid=self.next_rid, oid=oid)
        self.rooms[room.rid] = room
        self.user_room_map[oid] = room.rid
        return room

    def join_room(self, uid: int, rid: int):
        """
        加入房间
        :param uid: 用户id
        :param rid: 房间id
        :return: Bool
        """
        if uid in self.user_room_map:
            # 用户已在房间中
            return False
        room = self.rooms.get(rid)
        if not room:
            return False

        if len(room.players) >= room.max_players:
            # 房间满员
            return False
        if room.status != "waiting":
            # 房间不在[等待]状态
            return False
        room.players.append(uid)
        self.user_room_map[uid] = rid
        return True

    def leave_room(self, uid: int):
        """
        离开房间
        :param uid:
        :return:
        """
        rid = self.user_room_map.get(uid)
        if not rid:
            return
        room = self.rooms.get(rid)
        if not room:
            return
        # 删除玩家
        for key, value in room.players.items():
            if value == uid:
                room.players[key] = None
                break
        # 删除映射
        del self.user_room_map[uid]
        # 房间没人

        # 房主退出
