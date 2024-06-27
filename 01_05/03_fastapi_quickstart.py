from fastapi import FastAPI  # FastAPI 为你的 API 提供了所有功能
import uvicorn

app = FastAPI()  # 这个实例将会是创建你所有 API 的主要交互对象


@app.get("/")  # 路径操作装饰器
async def home():  # 路径操作函数
    return {"user_id": 1207}


@app.get("/shop")
def shop():
    
    return {"shop": "..."}


if __name__ == "__main__":
    uvicorn.run("03_fastapi_quickstart:app", port=8080, reload=True)
