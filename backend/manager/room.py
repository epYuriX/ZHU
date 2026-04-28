# manager / room.py
from doctest import FAIL_FAST
from fastapi import WebSocket
from typing import Dict, List, Optional
import uuid
from schemas import ServerBroadcast, ServerMessage
from game import GameEngine


class Room:
    """
    房间
        room_id: 房间 id
        host_id: 房主 id
        room_name: 房间列表
    """

    def __init__(self, room_id: str, room_name: str, host_id: int):
        """
        初始化
        :param room_id:
        :param room_name:
        :param host_id:
        """
        self.room_id = room_id
        self.host_id = host_id
        self.room_name = room_name
        # 存储 {
        # "user_id": int,
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

    async def start_game_logic(self):
        """
        初始化
        :return:
        """
        user_ids = [p["user_id"] for p in self.players]
        self.engine = GameEngine(user_ids)
        return self.engine.get_game_state()


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

    async def join_room(self, room_id: str, user_id: int, ws: WebSocket):
        """
        玩家加入房间
        :param room_id: 房间ID
        :param user_id: 用户ID
        :param ws: WebSocket连接对象
        :return:
        """
        room = self.get_room(room_id)
        # 校验
        if not room:
            return {
                "status": "error",
                "msg": "房间不存在",
            }
        if room.status != "waiting":
            return {
                "status": "error",
                "msg": "房间非等待状态，无法加入",
            }
        if len(room.players) >= room.max_players:
            return {
                "status": "error",
                "msg": "房间已满",
            }
        if any(p["user_id"] == user_id for p in room.players):
            return {
                "status": "error",
                "msg": "你已在房间内"
            }
        player_data = {
            "user_id": user_id,
            "ws": ws,
            "is_ready": False,
        }
        room.players.append(player_data)
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_JOINED,
            "user_id": user_id,
            "msg": f"玩家 {user_id} 加入了房间"
        })
        return {
            "status": "success",
            "room_id": room_id,
        }

    async def leave_room(self, room_id: str, user_id: int):
        """
        退出房间
        :param room_id: 房间 id
        :param user_id: 用户 id
        :return:
        """
        room = self.get_room(room_id)
        if not room:
            return {
                "status": "error",
                "msg": "room not exist",
            }
        # 移除该玩家
        room.players = [p for p in room.players if p["user_id"] != user_id]
        # 房主离开则解散
        if user_id in room.host_id:
            await room.broadcast({
                "type": ServerBroadcast.ROOM_DISBANDED,
                "msg": "房间解散 - 房主已离开",
            })
            self.remove_room(room_id)
            return {
                "status": "disbanded",
            }
        # 房间为空则解散
        if not room.players:
            self.remove_room(room_id)
            return {
                "status": "empty",
            }
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_LEFT,
            "user_id": user_id,
        })
        return {
            "status": "success",
        }

    async def toggle_ready(self, room_id: str, user_id: int):
        """
        玩家切换准备状态
        :param room_id:
        :param user_id:
        :return:
        """
        room = self.get_room(room_id)
        if not room or room.status != "waiting":
            return
        for player in room.players:
            if player["user_id"] == user_id:
                player["is_ready"] = not player.get("is_ready", False)
                break
        # 广播
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_READY,
            "payload": {
                "user_id": user_id,
                "players_status": [
                    {
                        "user_id": p["user_id"],
                        "is_ready": p["is_ready"],
                    }
                    for p in room.players
                ]
            }
        })
        # 检查是否全员准备
        await self.check_start_game(room)

    async def check_start_game(self, room: Room):
        """
        是否可以开始游戏
        :param room:
        :return:
        """
        ready_count = sum(1 for p in room.players if p.get("is_ready", False))
        if ready_count == room.max_players:
            room.status = "playing"
            game_state = await room.start_game_logic()
            await room.broadcast({
                "type": ServerBroadcast.GAME_START,
                "payload": {
                    "status": room.status,
                    "msg": f" {room.max_players} 人模式，游戏开始",
                    "initial_state": game_state
                }
            })

    async def kick_player(self, room_id: str, operator_id: int, target_id: int):
        """
        房主踢人
        :param room_id:
        :param operator_id:
        :param target_id:
        :return:
        """
        room = self.get_room(room_id)
        if not room:
            return
        if operator_id != room.host_id:
            await room.send_to_player(operator_id, {
                "type": ServerMessage.ERROR,
                "msg": "只有房主可以踢人"
            })
            return
        target_player = next((p for p in room.players if p["user_id"] == target_id), None)
        if target_player:
            await target_player["ws"].send_json({
                "type": ServerMessage.ERROR,
                "msg": "你已飞升"
            })
            await target_player["ws"].close(code=1000)
            room.players = [p for p in room.players if p["user_id"] != target_id]
            await room.broadcast({
                "type": ServerBroadcast.PLAYER_LEFT,
                "user_id": target_id,
                "msg": f"玩家 {target_id} 已飞升"
            })


room_manager = RoomManager()
