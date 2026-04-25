# schemas / msgType.py
from enum import Enum


class PlayerAction(str, Enum):
    """
    操作类
    """
    JOIN_ROOM = "JOIN_ROOM"  # 加入房间
    READY = "READY"  # 准备 / 取消
    KICK_PLAYER = "KICK_PLAYER"  # 踢人
    SET_ROOM_MODE = "SET_ROOM_MODE" # 设置人数
    DISSOLVE_ROOM = "DISSOLVE_ROOM"  # 解散房间
    LEAVE_ROOM = "LEAVE_ROOM"  # 离开房间


class ServerMessage(str, Enum):
    """
    响应类
    """
    JOIN_SUCCESS = "JOIN_SUCCESS"  # 进入房间后告知新玩家房间配置
    ERROR = "ERROR"  # 报错，房间已满等


class ServerBroadcast(str, Enum):
    """
    广播类
    """
    PLAYER_JOINED = "PLAYER_JOINED"  # 房间 - 新玩家加入
    PLAYER_READY = "PLAYER_READY"  # 房间 - 玩家准备 / 取消准备
    PLAYER_LEFT = "PLAYER_LEFT" # 房间 - 玩家离开
    ROOM_MODE_CHANGED = "ROOM_MODE_CHANGED" # 人数修改
    ALL_READY = "ALL_READY"  # 所有人已就绪
    GAME_START = "GAME_START"  # 游戏开始
    GAME_OVER = "GAME_OVER"  # 游戏结束
    ROOM_DISBANDED = "ROOM_DISBANDED"  # 房间解散


class GameAction(str, Enum):
    """
    游戏操作（以后再设计）
    ? -> ?
    """
    buzhidao = "???"