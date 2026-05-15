# room/room.py
from game import Game


class Room:
    """
    房间
        rid: 房间id
        oid: 房主id
        players{}: 玩家列表(存玩家id)
        ready_players[]: 已准备玩家
        player_cnt: 当前玩家数
        max_players: 最大玩家数
        status: 房间状态 (waiting, ready, playing)
    方法列表
        __init__(rid, oid): 初始化
        start_game(): 开始游戏
    """

    def __init__(self, rid, oid):
        """
        初始化
        :param rid: 房间id
        :param oid: 房主id (owner id)
        """
        self.rid = rid
        self.oid = oid
        self.players = {
            "P1": oid,
            "P2": None,
            "P3": None,
            "P4": None
        }  # P1~P4 -> uid/None
        self.ready_players = set()
        self.player_cnt = 1
        self.max_players = 4
        self.game = None
        self.status = "waiting"  # waiting, ready, playing

    def start_game(self):
        """
        游戏开始
        :return:
        """
        self.game = Game(self)
        self.status = "playing"

    def ready(self, uid: int):
        """
        玩家准备
        :param uid:
        :return:
        """
        self.ready_players.add(uid)

    def unready(self, uid: int):
        """
        玩家取消准备
        :param uid:
        :return:
        """
        if uid in self.ready_players:
            self.ready_players.remove(uid)
