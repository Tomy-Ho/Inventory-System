from fastapi import FastAPI
from fastapi import APIRouter
from DataModels.UserData import User

user_app = APIRouter()

@user_app.post("/")
async def creat_User(user : User):
    await User.insert(user)
    print(user)
    return user

@user_app.get("/get_one_user_info")
async def get_One_User(userid : str, user : User):
    result = await User.get(userid)
    return result

@user_app.get("/get_all_user_list")
async def get_All_Users():
    return await User.find_all().to_list()

@user_app.delete("/clear_user_list")
async def delete_All_Users():
    delete_result = await User.find_all().delete()
    return {
        "status" : "success",
        "Users deleted" : delete_result.deleted_count
    }
