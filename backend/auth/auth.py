from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "nidiyanwodicu"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """
    加密密码
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    """
    验证密码
    :param plain:
    :param hashed:
    :return:
    """
    return pwd_context.verify(plain, hashed)


def create_token(data: dict):
    """
    生成 JWT
    :param data: 
    :return:
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
