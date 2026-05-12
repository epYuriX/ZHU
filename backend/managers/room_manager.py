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
            return False
        room = self.rooms.get(rid)
        if not room:
            return False
        # 房间满员
        if len(room.players) >= room.max_players:
            return False
        # 游戏已经开始
        if room.status != "waiting":
            return False
        room.players.append(uid)
        self.user_room_map[uid] = rid
        return True
