# handlers/room_handler.py
from managers import room_manager, connection_manager


async def handle_get_room_list(uid: int, msg: dict):
    """
    获取房间列表
    :param uid:
    :param msg:
    :return:
    """
    rooms = room_manager.get_room_list()
    rmsg = {
        "type": "ROOM_LIST",
        "data": {
            "rooms": rooms
        }
    }
    await connection_manager.send_to_player(uid, rmsg)


async def handle_create_room(uid: int, msg: dict):
    """
    创建房间
    :param uid:
    :param msg:
    :return:
    """
    room = room_manager.create_room(uid)
    if not room:
        rmsg = {
            "type": "CREATE_ROOM",
            "data": {
                "msg": "- error: 无法创建房间",
            },
        }
        await connection_manager.send_to_user(uid, rmsg)
        return
    rmsg = {
        "type": "CREATE_ROOM",
        "data": {
            "rid": room.rid,
            "players": room.players,
        },
    }
    await connection_manager.send_to_user(uid, rmsg)


async def handle_join_room(uid: int, msg: dict):
    """
    加入房间
    :param uid:
    :param msg:
    :return:
    """
    rid = msg.get("rid")
    success = room_manager.join_room(uid, rid)
    if not success:
        rmsg = {
            "type": "JOIN_ROOM",
            "data": {
                "msg": "- error: 加入房间失败",
            }
        }
        await connection_manager.send_to_user(uid, rmsg)
        return
    room = room_manager.rooms.get(rid)
    # 广播房间更新
    await broadcast_room(room)


async def handle_leave_room(uid: int, msg: dist):
    """
    退出房间
    :param uid:
    :param msg:
    :return:
    """
    room = room_manager.get_room_by_uid(uid)
    if not room:
        return
    rid = room.rid
    room_manager.leave_room(uid)
    room = room_manager.rooms.get(rid)
    if room:
        await broadcast_room(room)


async def handle_ready(uid: int, msg: dict):
    """
    准备 / 取消准备
    :param uid:
    :param msg:
    :return:
    """
    room = room_manager.get_room_by_uid(uid)
    if not room:
        return
    if uid in room.ready_players:
        room.unready(uid)
    else:
        room.ready(uid)
    await broadcast_room(room)


async def handle_start_game(uid: int, msg: dict):
    """
    开始游戏
    :param uid:
    :param msg:
    :return:
    """
    room = room_manager.get_room_by_uid(uid)
    if not room:
        return
    if room.oid != uid:
        return
    if room.player_cnt < 4:
        return
    if len(room.ready_players) != room.player_cnt:
        return
    room.start_game()
    await broadcast_room(room)


async def broadcast_room(room):
    """
    广播房间信息 同步房间状态
    :param room:
    :return:
    """
    for uid in room.players.values():
        if uid is None:
            continue
        rmsg = {
            "type": "ROOM_UPDATE",
            "data": {
                "room": {
                    "rid": room.rid,
                    "oid": room.oid,
                    "players": room.players,
                    "player_cnt": room.player_cnt,
                    "status": room.status
                }
            }
        }
        await connection_manager.send_to_user(uid, rmsg)
