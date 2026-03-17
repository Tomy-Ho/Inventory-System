from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from DataModels.UserData import UserIn, UserOut, UserResponseStatus
from typing import Union

user_app = APIRouter(prefix="/User", tags=["User"])

@user_app.post("/", response_model=UserOut, status_code=201)
async def creat_User(user : UserIn):
    await UserIn.insert(user)
    return user

@user_app.get("/get_user_by_name_and_age", response_model=list[UserOut])
async def get_specific_User(username : str, userage : int):
    result = await UserIn.find(UserIn.name == username and UserIn.age == userage).to_list()
    
    if not result:
        raise HTTPException(status_code=404, detail="No user found.")
        
    return result

@user_app.get("/get_all_user_list", response_model=list[UserOut])
async def get_All_Users():
    return await UserIn.find_all().to_list()

@user_app.delete("/clear_user_list", response_model=UserResponseStatus)
async def delete_All_Users():
    delete_result = await UserIn.find_all().delete()
    return UserResponseStatus(status="success", details="amount deleted = %s" %delete_result.deleted_count)

@user_app.delete("/remove_user", response_model=UserResponseStatus)
async def delete_user(userid : str):
    find_user = await UserIn.get(userid)

    if not find_user:
        raise HTTPException(status_code=404, detail="User not found.")

    await UserIn.delete(find_user)
    return UserResponseStatus(status="success", details="User deleted = %s" %userid)

@user_app.put("/change_user_values", response_model=UserResponseStatus)
async def update_User_Data(userid : str, newUserData : UserOut):
    old_User = await UserIn.get(userid)

    if not old_User:
        raise HTTPException(status_code=404, detail="No User found.")
    
    old_User.name = newUserData.name
    old_User.age = newUserData.age
    old_User.email = newUserData.email

    await old_User.save()

    return UserResponseStatus(status="success", details="user updated = %s" %old_User)