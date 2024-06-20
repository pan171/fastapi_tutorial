from fastapi import APIRouter

user = APIRouter()


@user.post("/login")
def user_login():
    return {"user": "login"}


@user.get("/reg")
def user_reg():
    return {"user": "reg"}