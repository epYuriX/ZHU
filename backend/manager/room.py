# manager/room.py
from game import GameEngine
from typing import List, Dict, Optional


class Room:
    """
    房间
        rid: 房间 id
        host_id: 房主 id
        room_name: 房间列表
    """

    def __init__(self, rid: str, room_name: str, host_id: int):
        """
        初始化
        :param rid:
        :param room_name:
        :param host_id:
        """
        self.rid = rid
        self.host_id = host_id
        self.room_name = room_name
        # 存储 {
        # "uid": int,
        # "ws": WebSocket,
        # "is_ready": bool,
        # }
        self.players: List[Dict] = []
        self.max_players = 4
        self.status = "waiting"  # waiting (等待中) 或 playing (游戏中)
        self.engine: Optional[GameEngine] = None

    async def set_mode(self, mode: int):
        """
        模式切换 - 人数
        :param mode: 3 / 4
        :return:
        """
        if mode not in [3, 4]:
            return False, "无效的模式"
        if mode == 3 and len(self.players) > 3:
            return False, "当前人数超过3人，无法切换为3人模式"
        self.max_players = mode
        return True, f"已切换为 - {mode} - 人模式"

    async def send_to_player(self, uid, message: dict):
        """
        给特定用户发消息
        :param uid:
        :param message:
        :return:
        """
        for player in self.players:
            if player["uid"] == uid:
                await player["ws"].send_json(message)
                break

    async def broadcast(self, message: dict):
        """
        房间内广播
        :param message:
        :return:
        """
        for player in self.players:
            await player["ws"].send_json(message)

    async def start_game_logic(self):
        """
        初始化
        :return:
        """
        user_ids = [p["uid"] for p in self.players]
        self.engine = GameEngine(user_ids)
        return self.engine.get_game_state()
