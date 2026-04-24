# routers / user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin
from auth.auth import hash_password, verify_password, create_token

# 创建路由对象，可以添加前缀和标签
router = APIRouter(
    prefix="/user",  # 自动为下面所有接口加上 /users 前缀
    tags=["用户模块"]  # 在 Swagger 文档中自动归类
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    user register
    :param user:
    :param db:
    :return:
    """
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    new_user = User(
        username=user.username,
        name=user.name,
        password_hash=hash_password(user.password),
        email=user.email,
        phone=user.phone,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "注册成功"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    user login
    :param user:
    :param db:
    :return:
    """
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="用户不存在")
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="密码错误")
    token = create_token({"sub": db_user.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
