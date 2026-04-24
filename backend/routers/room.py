# routers / room.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from manager import room_manager

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


@router.websocket("/ws/{room_id}/{userid}")
async def join_room(websocket: WebSocket, room_id: str, userid: int):
    """
    加入房间
    :param websocket:
    :param room_id:
    :param userid:
    :return:
    """
    room = room_manager.get_room(room_id)
    if not room:
        await websocket.close(reason="房间不存在")
        return
    if len(room.members) >= room.max_players:
        await websocket.close(reason="房间已满")
        return
    await websocket.accept()
    room.players.append({
        "user_id": userid,
        "ws": websocket,
    })
    # 玩家进入房间通知
    await room.broadcast({
        "room_id": room.room_id,
        "user_id": userid,
    })
    try:
        while True:
            data = await websocket.receive_json()
            await room.broadcast({
                "event": "action",
                "user_id": userid,
                "data": data
            })
    except WebSocketDisconnect:
        await room_manager.leave_room(room_id, userid)


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
