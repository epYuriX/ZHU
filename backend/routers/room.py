# routers / room.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from manager import room_manager
from schemas import PlayerAction, ServerMessage, ServerBroadcast, GameAction

router = APIRouter(
    prefix="/room",
    tags=["房间模块"]
)


@router.get("/list")
async def list_rooms():
    """
    获取房间列表
    :return:
    """
    return room_manager.get_room_list()


@router.websocket("/ws/{room_id}/{user_id}")
async def join_room(websocket: WebSocket, room_id: str, user_id: int):
    """
    加入房间
    :param websocket:
    :param room_id:
    :param user_id:
    :return:
    """
    room = room_manager.get_room(room_id, user_id)
    # 检查
    if not room:
        await websocket.close(reason="房间不存在")
        return
    if len(room.players) >= room.max_players:
        await websocket.accept()
        await websocket.send_json({
            "type": ServerMessage.ERROR,
            "msg": "房间已满"
        })
        await websocket.close()
        return
    # 入库
    await websocket.accept()
    new_player = {
        "user_id": user_id,
        "ws": websocket,
        "is_ready": False,
    }
    room.players.append(new_player)
    # 告知新玩家当前房间信息
    await websocket.send_json({
        "type": ServerMessage.JOIN_SUCCESS,
        "payload": {
            "room_id": room.room_id,
            "room_name": room.room_name,
            "host_id": room.host_id,
            "players": [
                {
                    "user_id": p["user_id"],
                    "is_ready": p["is_ready"],
                }
                for p in room.players
            ]
        }
    })
    await room.broadcast({
        "type": ServerBroadcast.PLAYER_JOINED,
        "user_id": user_id,
    })
    try:
        while True:
            data = await websocket.receive_json()
            msg_type = data.get("type")
            if msg_type == PlayerAction.READY:
                await room_manager.toggle_ready(room_id, user_id)
            # - 预留
            elif msg_type == "???":
                if room.status == "playing":
                    await room.broadcast({
                        "type": "???",
                        "user_id": user_id,
                        "data": data.get("???")
                    })
    except WebSocketDisconnect:
        await room_manager.leave_room(room_id, user_id)


@router.post("/create")
async def create_room(room_name: str, user_id: int):
    """
    创建新房间
    :param room_name:
    :param user_id:
    :return:
    """
    room = room_manager.create_room(room_name, user_id)
    return {"room_id": room.room_id, "status": "created"}


@router.post("/leave")
async def leave_room(room_id: str, user_id: int):
    """
    主动退出房间
    :param room_id:
    :param user_id:
    :return:
    """
    result = await room_manager.leave_room(room_id, user_id)
    return result
