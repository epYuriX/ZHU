# manager / room.py
from fastapi import WebSocket
from typing import Dict, List, Optional
import uuid


class Room:
    """
    房间
    """

    def __init__(self, room_id: str, room_name: str, host_id: int):
        """
        初始化
        :param room_id:
        :param room_name:
        :param host_id:
        """
        self.room_id = room_id
        self.room_name = room_name
        self.host_id = host_id
        # 存储 {
        # "user_id": int,
        # "ws": WebSocket,
        # "is_ready": bool,
        # }
        self.players: List[Dict] = []
        self.max_players = 4
        self.status = "waiting"  # waiting (等待中) 或 playing (游戏中)

    async def send_to_player(self, user_id, message: dict):
        """
        给特定用户发消息
        :param user_id:
        :param message:
        :return:
        """
        for player in self.players:
            if player["user_id"] == user_id:
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


class RoomManager:
    """
    房间管理器
    """

    def __init__(self):
        self.active_rooms: Dict[str, Room] = {}

    def get_room_list(self):
        """
        get room list
        :return:
        """
        return [
            {
                "room_id": r.room_id,
                "room_name": r.room_name,
                "player_count": len(r.players),
            }
            for r in self.active_rooms.values()
        ]

    def create_room(self, room_name: str, host_id: int):
        """
        new room
        :param room_name:
        :param host_id:
        :return:
        """
        room_id = str(uuid.uuid4())[:8]
        new_room = Room(room_id, room_name, host_id)
        self.active_rooms[room_id] = new_room
        return new_room

    def get_room(self, room_id: str) -> Optional[Room]:
        return self.active_rooms.get(room_id)

    def remove_room(self, room_id: str):
        """
        remove room
        :param room_id: 房间 id
        :return:
        """
        if room_id in self.active_rooms:
            del self.active_rooms[room_id]

    async def leave_room(self, room_id: str, user_id: int):
        """
        退出房间
        :param room_id: 房间 id
        :param user_id: 用户 id
        :return:
        """
        if room_id not in self.active_rooms:
            return {
                "status": "error",
                "msg": "room not exist",
            }
        room = self.active_rooms[room_id]
        # 移除该玩家
        room.players = [p for p in room.players if p["user_id"] != user_id]
        # 房主离开则解散
        if user_id == room.host_id:
            await room.broadcast({
                "event": "room_disbanded",
                "msg": "房主已离开，房间解散",
            })
            self.remove_room(room_id)
            return {
                "status": "disbanded",
                "msg": "房间已解散",
            }
        # 房间为空则解散
        if not room.players:
            self.remove_room(room_id)
            return {
                "status": "empty",
                "msg": "房间已销毁",
            }
        await room.broadcast({
            "event": "player_left",
            "user_id": user_id,
        })
        return {
            "status": "success",
            "msg": "已退出房间"
        }

    async def toggle_ready(self, room_id: str, user_id: int):
        """

        :param room_id:
        :param user_id:
        :return:
        """
        room = self.get_room(room_id)
        if not room or room.status != "waiting":
            return
        for player in room.players:
            if player["user_id"] == user_id:
                player["is_ready"] = !player.get("is_ready", False)
                break
        # 广播
        await room.broadcast({
            "event": "player_status_change",
            "user_id": user_id,
            "players_status": [
                {
                    "user_id": p["user_id"],
                    "is_ready": p.get("is_ready", False),
                }
                for p in room.players
            ]
        })
        # 检查是否可以开始游戏
        await self.check_start_game(room)

    async def check_start_game(self, room: Room):
        ready_count = sum(1 for p in room.players if p.get("is_ready", False))
        if ready_count >= 3 and ready_count == len(room.players):
            room.status = "playing"
            await room.broadcast({
                "event": "game_start",
                "msg": "全员就绪，游戏开始",
                "status": room.status,
            })


room_manager = RoomManager()
