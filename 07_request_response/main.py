from fastapi import FastAPI
from app.app01 import app01
import uvicorn

app = FastAPI()

app.include_router(app01, tags=["01 路径参数"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
