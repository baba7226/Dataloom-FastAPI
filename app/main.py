# 导入FastAPI框架
from fastapi import FastAPI
# 导入自定义的路由
from app.api.routes import router

# 创建FastAPI应用实例
app = FastAPI(
    title="Data Loom Cleaning",
    version="1.0"
)

# 把自定义的路由注册到应用
app.include_router(router)