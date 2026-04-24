from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import user_router, room_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源（仅供测试使用，生产环境请指定具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有请求方法 (GET, POST 等)
    allow_headers=["*"],  # 允许所有请求头
)
app.include_router(user_router)
app.include_router(room_router)


@app.get("/")
def root():
    """
    :return:
    """
    return {"msg": "ok"}
