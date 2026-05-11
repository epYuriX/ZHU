# managers/connection_manager.py
from starlette.websockets import WebSocket


class ConnectionManager:
    """
    WebSocket 连接管理器
    """

    def __init__(self):
        """
        初始化
        """
        # uid -> websocket
        self.connections = {}

    async def connect(self, uid: int, websocket: WebSocket):
        """
        添加连接
        :param uid:
        :param websocket:
        :return:
        """
        await websocket.accept()
        self.connections[uid] = websocket
        print(f"用户 {uid} 已连接, 当前连接数: {len(self.connections)}")

    def disconnect(self, uid: int):
        """
        断开连接
        :param uid:
        :return:
        """
        if uid in self.connections:
            del self.connections[uid]
            print(f"用户 {uid} 已断开, 当前连接数: {len(self.connections)}")

    async def send_to_user(self, uid: int, msg: dict):
        """
        发送消息给指定用户
        :param uid:
        :param msg:
        :return:
        """
        websocket = self.connections.get(uid)
        if websocket:
            await websocket.send_json(msg)

    async def broadcast(self, uids: list, msg: dict):
        """
        列表广播
        :param uids:
        :param msg:
        :return:
        """
        for uid in uids:
            websocket = self.connections.get(uid)
            if websocket:
                await websocket.send_json(msg)
