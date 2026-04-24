# schemas / auth.py
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    name: str
    password: str
    email: str
    phone: str


class UserLogin(BaseModel):
    username: str
    password: str
