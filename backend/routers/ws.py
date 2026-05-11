# routers/ws.py
from fastapi import WebSocket
from starlette.websockets import WebSocketDisconnect
from auth.auth import verify_token

router = APIRouter(
    prefix="/ws",
    tags=["websocket长连接"]
)


@router.websocket("")
async def websocket_connect(websocket: WebSocket):
    """
    建立websocket长连接
    :param websocket:
    :return:
    """
    # 验证token
    token = websocket.query_params.get("token")
    if not token:
        await websocket.close(code=1008)
        return
    payload = verify_token(token)
    if not payload:
        await websocket.close(code=1008)
        return
    # 接受连接
    await websocket.accept()
    try:
        while True:
            msg = await websocket.receive_json()
            await websocket.send_json({"echo": msg})
            # 处理
    except WebSocketDisconnect:
        # 连接断开
        pass
