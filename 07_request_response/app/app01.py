from fastapi import APIRouter


app01 = APIRouter()


# 路由匹配顺序和函数出现顺序有关
@app01.get("/user/1")
def get_user():
    return {"user_id": "root"}


@app01.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app01.get("/article/{article_id}")
def get_article(article_id: int):
    return {"user_id": article_id}
