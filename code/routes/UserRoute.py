from fastapi import FastAPI, HTTPException
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

@user_app.put("/change_user_values")
async def update_User_Data(userid : str, newUserData : User):
    old_User = await User.get(userid)

    if not old_User:
        raise HTTPException(status_code=404, detail="No User found.")
    
    old_User.name = newUserData.name
    old_User.age = newUserData.age
    old_User.email = newUserData.email
    old_User.password = newUserData.password

    await old_User.save()

    return{
        "status" : "success",
        "User updated" : old_User
    }