# 接口文档 — 账户系统 与 房间系统

本文件基于后端代码（位于 `backend/`）自动提取并整理，包含账户（User）与房间（Room）相关的 HTTP 与 WebSocket 接口规范、请求/响应示例、鉴权说明及实现细节提醒。

---

## 检查清单
- [x] 提取并描述账户相关接口（注册、登录）
- [x] 提取并描述房间相关 HTTP 接口（房间列表、创建、离开）
- [x] 提取并描述房间 WebSocket 接口（连接鉴权、消息/广播规范、示例）
- [x] 给出鉴权（JWT）细节与安全建议

---

## 概要
- 后端框架：FastAPI（`backend/main.py`）
- 数据库：SQLite（`backend/database.py`，`sqlite:///./test.db`）
- 鉴权：JWT（`backend/auth/auth.py`），token 有效期 2 小时
- CORS：允许所有来源（`allow_origins=["*"]`）

---

## 鉴权说明（Auth）
- Token 生成：`create_token(data: dict)`（`backend/auth/auth.py`）
  - 使用 HS256（`SECRET_KEY="nidiyanwodicu"`）
  - 自动在 payload 中加入 `exp` = UTC now + 2 hours
  - 登录返回示例：`{"access_token": "<JWT>", "token_type": "bearer"}`
- Token 校验：`verify_token(token: str)`，返回 payload 或 `None`
- WebSocket 鉴权：连接 `/room/ws/{rid}` 时需通过 query 参数 `token` 提供 JWT，验证失败会关闭连接（close code: `WS_1008_POLICY_VIOLATION`）。

---

## 共享枚举与消息类型（摘自 `backend/schemas/msgType.py`）
- PlayerAction（客户端操作）：
  - `JOIN_ROOM`, `READY`, `KICK_PLAYER`, `SET_ROOM_MODE`, `DISSOLVE_ROOM`, `LEAVE_ROOM`
- ServerMessage（服务端对单个客户端的响应）：
  - `JOIN_SUCCESS`, `ERROR`
- ServerBroadcast（房间广播）：
  - `PLAYER_JOINED`, `PLAYER_READY`, `PLAYER_LEFT`, `ROOM_MODE_CHANGED`, `ALL_READY`, `GAME_START`, `GAME_OVER`, `ROOM_DISBANDED`
- GameAction：游戏内部操作（会转发到 game engine），例如 `SELECT_POSITION`

---

## 数据模型（用户）
（参见 `backend/models/user.py`）
- User 字段：
  - `uid` (Integer, 主键)
  - `username` (String, unique)
  - `name` (String, unique)
  - `password_hash` (String)
  - `lv`, `win`, `email`, `phone`, `created_at`, `last_login_at`, `status`

---

## API 细节

所有路由前缀：
- 账户模块前缀：`/user`（见 `backend/routers/user.py`）
- 房间模块前缀：`/room`（见 `backend/routers/room.py`）

### 一、账户系统（User）HTTP 接口

1) POST /user/register
- 描述：用户注册
- 请求 Body（JSON，Pydantic `UserCreate`）：
  - `username`: str（必填）
  - `name`: str（必填）
  - `password`: str（必填）
  - `email`: str
  - `phone`: str
- 成功响应：200
  - `{"msg": "注册成功"}`
- 常见错误：400 用户名已存在 -> `{"detail": "用户名已存在"}`
- 实现要点：使用 `hash_password` 保存 `password_hash`，并在 DB 中创建记录。

示例（curl）：

```bash
curl -X POST "http://localhost:8000/user/register" \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","name":"Alice","password":"pwd123","email":"a@example.com","phone":"123"}'
```

2) POST /user/login
- 描述：用户登录并返回 JWT
- 请求 Body（JSON，Pydantic `UserLogin`）：
  - `username`: str（必填）
  - `password`: str（必填）
- 成功响应：200
  - `{"access_token": "<JWT>", "token_type": "bearer"}`
- 常见错误：400 用户不存在 / 密码错误 -> `{"detail": "用户不存在"}` 或 `{"detail": "密码错误"}`
- 实现要点：验证密码使用 `verify_password`，生成 token 使用 `create_token({"sub": username, "uid": uid})`。

示例（curl）：

```bash
curl -X POST "http://localhost:8000/user/login" \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"pwd123"}'
```

---

### 二、房间系统（Room）HTTP 接口

1) GET /room/list
- 描述：获取当前活跃房间列表
- 请求：GET
- 响应：200 JSON 数组，每项：
  - `rid`: str
  - `room_name`: str
  - `player_count`: int
- 实现：`room_manager.get_room_list()` 返回 `active_rooms` 的摘要。

示例响应：

```json
[{"rid": "a1b2c3d4", "room_name": "房间A", "player_count": 2}]
```

2) POST /room/create
- 描述：创建新房间
- 请求参数（函数签名为 `create_room(room_name: str, uid: int)`，可通过表单或查询提交）：
  - `room_name`: str（必填）
  - `uid`: int（必填，房主用户 id）
- 成功响应：200
  - `{"rid": "<new_rid>", "status": "created"}`
- 实现要点：使用 `RoomManager.create_room()` 生成 `rid`（uuid 前 8 位）并缓存房间对象。

示例（curl，form）：

```bash
curl -X POST "http://localhost:8000/room/create" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "room_name=测试房&uid=1"
```

3) POST /room/leave
- 描述：主动离开房间
- 请求参数：
  - `rid`: str
  - `uid`: int
- 响应：返回 `room_manager.leave_room(rid, uid)` 的结果，可能包含：
  - `{"status": "success"}`
  - `{"status": "disbanded"}`（房主离开导致解散）
  - `{"status": "empty"}`（房间空了）
  - `{"status": "error", "msg": "room not exist"}`

示例（curl）：

```bash
curl -X POST "http://localhost:8000/room/leave" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "rid=a1b2c3d4&uid=1"
```

---

### 三、房间系统 — WebSocket 实时接口

- 路由：WebSocket `ws://<host>/room/ws/{rid}?token=<JWT>`
- 必需：Query 参数 `token`（JWT，由登录接口获得）

连接 & 入房流程：
1. 客户端用带 token 的 URL 建立 WebSocket 连接。
2. 服务端通过 `verify_token(token)` 验证；失败则 `websocket.close(code=WS_1008_POLICY_VIOLATION)`。
3. 验证通过后服务端 `await websocket.accept()` 并调用 `room_manager.join_room(rid, uid, websocket)` 完成入房并广播 `PLAYER_JOINED`。
4. 服务端向新加入客户端发送入房快照（`ServerMessage.JOIN_SUCCESS`）。之后开始监听客户端消息循环。

入房快照示例（Server -> 新玩家）：

```json
{
  "type": "JOIN_SUCCESS",
  "payload": {
	"rid": "a1b2c3d4",
	"room_name": "房间A",
	"host_id": 1,
	"players": [{"uid": 1, "is_ready": false}, {"uid": 2, "is_ready": true}]
  }
}
```

客户端可发送的消息（JSON）示例：
- 切换准备（READY）

```json
{"type": "READY"}
```

- 踢人（KICK_PLAYER）

```json
{"type": "KICK_PLAYER", "payload": {"target_id": 3}}
```

- 设置房间模式（SET_ROOM_MODE）

```json
{"type": "SET_ROOM_MODE", "payload": {"mode": 3}}
```

- 游戏相关动作（转发给 game engine，例如 SELECT_POSITION）

```json
{"type": "SELECT_POSITION", "payload": {"position": 2}}
```

服务端广播/消息示例：
- 新玩家加入（广播）：

```json
{"type": "PLAYER_JOINED", "uid": 4, "msg": "玩家 4 加入了房间"}
```

- 玩家准备状态更新（广播）：

```json
{
  "type": "PLAYER_READY",
  "payload": {
	"uid": 2,
	"players_status": [{"uid":1,"is_ready":true}, {"uid":2,"is_ready":false}]
  }
}
```

- 房间模式变更（广播）：

```json
{"type": "ROOM_MODE_CHANGED", "payload": {"max_players": 3, "msg": "已切换为 - 3 - 人模式"}}
```

- 游戏开始（广播）：

```json
{
  "type": "GAME_START",
  "payload": {
    "status": "playing",
    "msg": "4 人模式，游戏开始",
    "initial_state": {}
  }
}
```

- 错误消息（单个客户端）：

```json
{"type": "ERROR", "msg": "你已在房间内"}
```

断线/离开：
- 客户端断开（WebSocketDisconnect）或主动调用 `/room/leave` 会触发 `room_manager.leave_room`，服务端会广播 `PLAYER_LEFT` 或 `ROOM_DISBANDED`（若房主离开）。

示例 JS 客户端连接：

```javascript
const token = '<JWT_FROM_LOGIN>';
const rid = 'a1b2c3d4';
const ws = new WebSocket(`ws://localhost:8000/room/ws/${rid}?token=${encodeURIComponent(token)}`);
ws.onmessage = ev => console.log('recv', JSON.parse(ev.data));
ws.onopen = () => ws.send(JSON.stringify({type: 'READY'}));
```

---

## 错误码与行为约定
- HTTP:
  - 400：常用于账户相关错误（用户不存在、用户名已存在、密码错误等）
- WebSocket:
  - 鉴权失败 -> 立即关闭（WS_1008_POLICY_VIOLATION）
  - 被房主踢 -> 服务端先 `send_json` 一个 `ERROR`，随后 `close(code=1000)`（见 `kick_player` 实现）

---

## 实现建议与注意事项
- 为 `/room/create` 和 `/room/leave` 使用 Pydantic 请求体会更规范（当前为函数参数，FastAPI 将其视为查询或表单参数）。
- 不要在生产仓库中将 `SECRET_KEY` 明文提交，建议使用环境变量。
- CORS 当前放宽为 `*`，生产环境请按需收紧。
- 增加日志与异常监控，避免单个 WebSocket 发送失败影响整个广播流程。

---

## 快速索引（接口一览）
- POST /user/register — 用户注册
- POST /user/login — 用户登录（返回 JWT）
- GET /room/list — 房间列表
- POST /room/create — 创建房间
- POST /room/leave — 主动离开房间
- WS /room/ws/{rid}?token=... — 房间实时通道（WebSocket）

---

如需我将 `/room/create` 与 `/room/leave` 改为使用 Pydantic 请求体并修改路由实现、或者生成更完整的 WebSocket 测试脚本（自动化脚本或简单 Node/Python 客户端），我可以继续修改并在工作区提交更改。


