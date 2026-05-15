# dispatcher.py
from protocol import *
from handlers import *


class Dispatcher:
    """
    消息分发器
    方法目录
        __init__(): 初始化
        register(): 注册处理程序
        despatch(): 处理程序分发
    """

    def __init__(self):
        """
        初始化
        """
        # action -> handler
        self.handlers = {}

    def register(self, action: str, handler):
        """
        注册处理程序
        :param action:
        :param handler:
        :return:
        """
        self.handlers[action] = handler

    async def dispatch(self, uid: int, msg: dict):
        """
        分发处理程序
        :param uid:
        :param msg:
        :return:
        """
        action = msg.get("action")
        if not action:
            print("- error 消息没有 action 字段")
            return
        handler = self.handlers.get(action)
        if not handler:
            print(f"- error 没有找到action {action} 处理程序")
            return
        await handler(uid, msg)


dispatcher = Dispatcher()

dispatcher.register("READY", ready)
dispatcher.register("GET_ROOM_LIST", handle_get_room_list)
dispatcher.register("CREATE_ROOM", handle_create_room)
dispatcher.register("JOIN_ROOM", handle_join_room)
dispatcher.register("LEAVE_ROOM", handle_leave_room)
dispatcher.register("START_GAME", handle_start_game)
