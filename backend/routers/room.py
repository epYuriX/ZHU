# routers / room.py
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


@router.websocket("/ws/{room_id}")
async def ws_join_room(websocket: WebSocket, room_id: str, token: str = Query(...)):
    """
    加入房间 WebSocket 完整实现
    """
    # 鉴权
    payload = verify_token(token)
    if not payload:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return
    user_id = payload.get("user_id")
    # 调用管理器逻辑进行加入校验与入库
    result = await room_manager.join_room(room_id, user_id, websocket)
    if result["status"] == "error":
        # 如果校验失败（如房满），先 accept 再发错误消息，最后 close
        await websocket.accept()
        await websocket.send_json({
            "type": ServerMessage.ERROR,
            "msg": result["msg"]
        })
        await websocket.close()
        return
    # 校验通过，正式接受连接
    await websocket.accept()
    room = result["room"]
    # 告知新玩家当前房间的初始快照
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
    # 进入消息监听循环
    try:
        while True:
            data = await websocket.receive_json()
            msg_type = data.get("type")
            msg_payload = data.get("payload", {})
            #  准备 / 取消准备
            if msg_type == PlayerAction.READY:
                await room_manager.toggle_ready(room_id, user_id)
            # 房主踢人
            elif msg_type == PlayerAction.KICK_PLAYER:
                target_id = msg_payload.get("target_id")
                if target_id:
                    # 注意：Manager里的方法名是 kick_player
                    await room_manager.kick_player(room_id, user_id, target_id)
            # 设置房间模式 (3人/4人)
            elif msg_type == PlayerAction.SET_ROOM_MODE:
                if user_id != room.host_id:
                    await websocket.send_json({
                        "type": ServerMessage.ERROR,
                        "msg": "只有房主能修改模式",
                    })
                    continue
                new_mode = msg_payload.get("mode")
                success, msg = await room.set_mode(new_mode)
                if success:
                    await room.broadcast({
                        "type": ServerBroadcast.ROOM_MODE_CHANGED,
                        "payload": {
                            "max_players": room.max_players,
                            "msg": msg,
                        }
                    })
                else:
                    await websocket.send_json({
                        "type": ServerMessage.ERROR,
                        "msg": msg
                    })

            # 游戏进行中的指令转发 (预留)
            elif msg_type == GameAction.PREP_SELECT:
                # 示例：处理选位指令
                if room.status == "playing" and room.engine:
                    node_id = msg_payload.get("node_id")
                    res = await room.engine.handle_prep_select(user_id, node_id)
                    # 发送结果给所有人或发起者
                    await room.broadcast({
                        "type": ServerBroadcast.GAME_STATE_UPDATE,
                        "payload": {
                            "result": res,
                            "state": room.engine.get_game_state()
                        }
                    })
    except WebSocketDisconnect:
        # 掉线或关闭网页
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
