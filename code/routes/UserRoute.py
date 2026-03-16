from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from DataModels.UserData import UserIn, UserOut

user_app = APIRouter()

@user_app.post("/", response_model=UserOut)
async def creat_User(user : UserIn):
    await UserIn.insert(user)
    return user

@user_app.get("/get_user_by_name_and_age", response_model=list[UserOut])
async def get_specific_User(username : str, userage : int):
    result = await UserIn.find(UserIn.name == username and UserIn.age == userage).to_list()
    return result

@user_app.get("/get_all_user_list", response_model=list[UserOut])
async def get_All_Users():
    return await UserIn.find_all().to_list()

@user_app.delete("/clear_user_list")
async def delete_All_Users():
    delete_result = await UserIn.find_all().delete()
    return {
        "status" : "success",
        "Users deleted" : delete_result.deleted_count
    }

@user_app.put("/change_user_values")
async def update_User_Data(userid : str, newUserData : UserOut):
    old_User = await UserIn.get(userid)

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