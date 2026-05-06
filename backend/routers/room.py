# routers / room_manager.py
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, status
from manager import room_manager
from schemas import PlayerAction, ServerMessage, ServerBroadcast, GameAction
from auth.auth import verify_token

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


@router.websocket("/ws/{rid}")
async def ws_join_room(websocket: WebSocket, rid: str, token: str = Query(...)):
    """
    加入房间 WebSocket
    """
    # 鉴权并获取 uid
    uid = await _authenticate_ws(token, websocket)
    if not uid:
        return

    # 接受 websocket 连接后交给房间管理器处理（join_room 内会广播）
    await websocket.accept()

    # 调用管理器逻辑进行加入校验与入库
    result = await room_manager.join_room(rid, uid, websocket)
    if result["status"] == "error":
        # 如果校验失败，告诉客户端并关闭连接
        await websocket.send_json({"type": ServerMessage.ERROR, "msg": result["msg"]})
        await websocket.close()
        return

    # 校验通过，连接已被 accept
    room = result["room"]

    # 告知新玩家当前房间的初始快照
    await _send_join_snapshot(websocket, room)

    # 进入消息监听循环，所有消息由单独的处理器处理
    try:
        while True:
            data = await websocket.receive_json()
            await _handle_client_message(data, room, rid, uid, websocket)
    except WebSocketDisconnect:
        # 掉线或关闭网页
        await room_manager.leave_room(rid, uid)


@router.post("/create")
async def create_room(room_name: str, uid: int):
    """
    创建新房间
    :param room_name:
    :param uid:
    :return:
    """
    room = room_manager.create_room(room_name, uid)
    return {"rid": room.rid, "status": "created"}


@router.post("/leave")
async def leave_room(rid: str, uid: int):
    """
    主动退出房间
    :param rid:
    :param uid:
    :return:
    """
    result = await room_manager.leave_room(rid, uid)
    return result


async def _authenticate_ws(token: str, websocket: WebSocket):
    """
    验证 token 并返回 uid；鉴权失败时关闭 websocket 并返回 None。
    """
    payload = verify_token(token)
    if not payload:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return None
    return payload.get("uid")


async def _send_join_snapshot(websocket: WebSocket, room):
    """
    向新加入的 websocket 发送房间初始快照。
    """
    await websocket.send_json({
        "type": ServerMessage.JOIN_SUCCESS,
        "payload": {
            "rid": room.rid,
            "room_name": room.room_name,
            "host_id": room.host_id,
            "players": [
                {"uid": p["uid"], "is_ready": p["is_ready"]}
                for p in room.players
            ],
        }
    })


async def _handle_client_message(data: dict, room, rid: str, uid: int, websocket: WebSocket):
    """
    处理来自客户端的单条消息。

    注意：游戏内部的操作（如选位、出牌等）不应在路由层实现，
    这里只把这类消息统一转发给房间的 game engine 处理；
    非游戏操作仍由 room_manager / room 对象负责。
    """
    msg_type = data.get("type")
    msg_payload = data.get("payload", {})

    # 准备 / 取消准备
    if msg_type == PlayerAction.READY:
        await room_manager.toggle_ready(rid, uid)
        return

    # 房主踢人
    if msg_type == PlayerAction.KICK_PLAYER:
        target_id = msg_payload.get("target_id")
        if target_id:
            await room_manager.kick_player(rid, uid, target_id)
        return

    # 设置房间模式 (3人/4人)
    if msg_type == PlayerAction.SET_ROOM_MODE:
        if uid != room.host_id:
            await websocket.send_json({"type": ServerMessage.ERROR, "msg": "只有房主能修改模式"})
            return
        new_mode = msg_payload.get("mode")
        success, msg = await room.set_mode(new_mode)
        if success:
            await room.broadcast({
                "type": ServerBroadcast.ROOM_MODE_CHANGED,
                "payload": {"max_players": room.max_players, "msg": msg},
            })
        else:
            await websocket.send_json({"type": ServerMessage.ERROR, "msg": msg})
        return

    # 游戏内操作统一交由 game engine 处理（路由层不实现具体游戏逻辑）
    # 如果房间正在游戏中并且 engine 可用，则将消息转发给 engine 的通用入口。
    # 这样可以让游戏逻辑集中在 engine 中，降低路由和房间管理的耦合度。
    if room.status == "playing" and getattr(room, "engine", None):
        try:
            # 优先使用 engine 提供的通用处理接口
            if hasattr(room.engine, "handle_client_message"):
                await room.engine.handle_client_message(uid, msg_type, msg_payload)
            else:
                # 退回到旧的具体接口（如果 engine 提供），兼容现有实现
                if msg_type == GameAction.PREP_SELECT and hasattr(room.engine, "handle_prep_select"):
                    node_id = msg_payload.get("node_id")
                    res = await room.engine.handle_prep_select(uid, node_id)
                    await room.broadcast({
                        "type": ServerBroadcast.GAME_STATE_UPDATE,
                        "payload": {"result": res, "state": room.engine.get_game_state()},
                    })
                else:
                    # 如果 engine 提供未知动作的统一处理函数也可以调用
                    if hasattr(room.engine, "handle_unknown_action"):
                        await room.engine.handle_unknown_action(uid, msg_type, msg_payload)
        except Exception:
            # 防止 engine 内部错误导致 websocket 断开，向客户端返回通用错误提示
            await websocket.send_json({"type": ServerMessage.ERROR, "msg": "游戏操作处理失败"})
        return
