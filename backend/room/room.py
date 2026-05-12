# room/room.py

class Room:
    """
    房间
        rid: 房间id
        oid: 房主id
        players{}: 玩家列表(存玩家id)
        max_players: 最大玩家数
        status: 房间状态 (waiting, ready, playing)
    """

    def __init__(self, rid, oid):
        """
        初始化
        :param rid: 房间id
        :param oid: 房主id (owner id)
        """
        self.rid = rid
        self.oid = oid
        self.players = {"P1": None, "P2": None, "P3": None, "P4": None}  # P1~P4 -> uid/None
        self.max_players = 4
        self.status = "waiting"  # waiting, ready, playing

