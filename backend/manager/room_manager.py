# manager/room_manager.py
from fastapi import WebSocket
from typing import Dict, Optional
import uuid
from schemas import ServerBroadcast, ServerMessage


class RoomManager:
    """
    房间管理器
    """

    def __init__(self):
        self.active_rooms: Dict[str, Room] = {}

    def get_room_list(self):
        """
        获取房间列表
        :return: 房间列表[]:
                    rid: 房间id
                    room_name: 房间名
                    player_count: 房间人数
        """
        return [
            {
                "rid": r.rid,
                "room_name": r.room_name,
                "player_count": len(r.players),
            }
            for r in self.active_rooms.values()
        ]

    def create_room(self, room_name: str, host_id: int):
        """
        创建房间
        :param room_name:
        :param host_id:
        :return:
        """
        rid = str(uuid.uuid4())[:8]
        new_room = Room(rid, room_name, host_id)
        self.active_rooms[rid] = new_room
        return new_room

    def get_room(self, rid: str) -> Optional[Room]:
        return self.active_rooms.get(rid)

    def remove_room(self, rid: str):
        """
        remove room
        :param rid: 房间 id
        :return:
        """
        if rid in self.active_rooms:
            del self.active_rooms[rid]

    async def join_room(self, rid: str, uid: int, ws: WebSocket):
        """
        玩家加入房间
        """
        room = self.get_room(rid)
        # 校验
        if not room:
            return {
                "status": "error",
                "msg": "房间不存在",
            }
        if room.status != "waiting":
            return {
                "status": "error",
                "msg": "游戏已开始，无法加入",
            }
        if len(room.players) >= room.max_players:
            return {
                "status": "error",
                "msg": "房间已满",
            }
        if any(p["uid"] == uid for p in room.players):
            return {
                "status": "error",
                "msg": "你已在房间内",
            }

        # 入库
        player_data = {
            "uid": uid,
            "ws": ws,
            "is_ready": False,
        }
        room.players.append(player_data)
        # 广播
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_JOINED,
            "uid": uid,
            "msg": f"玩家 {uid} 加入了房间"
        })
        return {"status": "success", "room": room}

    async def leave_room(self, rid: str, uid: int):
        """
        退出房间
        :param rid: 房间id
        :param uid: 用户id
        :return:
        """
        room = self.get_room(rid)
        if not room:
            return {
                "status": "error",
                "msg": "room not exist",
            }
        # 移除该玩家
        room.players = [p for p in room.players if p["uid"] != uid]
        # 房主离开则解散
        if uid == room.host_id:
            await room.broadcast({
                "type": ServerBroadcast.ROOM_DISBANDED,
                "msg": "房间解散 - 房主已离开",
            })
            self.remove_room(rid)
            return {
                "status": "disbanded",
            }
        # 房间为空则解散
        if not room.players:
            self.remove_room(rid)
            return {
                "status": "empty",
            }
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_LEFT,
            "uid": uid,
        })
        return {
            "status": "success",
        }

    async def toggle_ready(self, rid: str, uid: int):
        """
        玩家切换准备状态
        :param rid:
        :param uid:
        :return:
        """
        room = self.get_room(rid)
        if not room or room.status != "waiting":
            return
        for player in room.players:
            if player["uid"] == uid:
                player["is_ready"] = not player.get("is_ready", False)
                break
        # 广播
        await room.broadcast({
            "type": ServerBroadcast.PLAYER_READY,
            "payload": {
                "uid": uid,
                "players_status": [
                    {
                        "uid": p["uid"],
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

    async def kick_player(self, rid: str, operator_id: int, target_id: int):
        """
        房主踢人
        :param rid:
        :param operator_id:
        :param target_id:
        :return:
        """
        room = self.get_room(rid)
        if not room:
            return
        if operator_id != room.host_id:
            await room.send_to_player(operator_id, {
                "type": ServerMessage.ERROR,
                "msg": "只有房主可以踢人"
            })
            return
        target_player = next((p for p in room.players if p["uid"] == target_id), None)
        if target_player:
            await target_player["ws"].send_json({
                "type": ServerMessage.ERROR,
                "msg": "你已飞升"
            })
            await target_player["ws"].close(code=1000)
            room.players = [p for p in room.players if p["uid"] != target_id]
            await room.broadcast({
                "type": ServerBroadcast.PLAYER_LEFT,
                "uid": target_id,
                "msg": f"玩家 {target_id} 已飞升"
            })






room_manager = RoomManager()
