# managers/__init__.py
from .room_manager import room_manager
from .connection_manager import ConnectionManager

# 全局创建 managers
connection_manager = ConnectionManager()
