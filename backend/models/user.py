#models / auth.py
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    """
    user table:
        uid: 用户id
        username: 用户名
        name: 昵称
        password_hash: 密码哈希值
        lv: 等级
        win: 胜场
        email: 邮箱
        phone: 电话
        created_at: 注册时间
        last_login_at: 最后登录时间
        status: 帐号状态
    """
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    password_hash = Column(String)
    lv = Column(Integer)
    win = Column(Integer)
    email = Column(String)
    phone = Column(String)
    created_at = Column(String)
    last_login_at = Column(String)
    status = Column(String)
