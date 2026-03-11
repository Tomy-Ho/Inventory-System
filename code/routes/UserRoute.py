from fastapi import FastAPI
from fastapi import APIRouter
from DataModels.UserData import User

user_app = APIRouter()

@user_app.post("/")
async def creat_User(user : User):
    await User.insert(user)
    return user