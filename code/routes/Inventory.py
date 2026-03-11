from fastapi import FastAPI
from fastapi import APIRouter
from DataModels.InventoryData import InventoryItem

inv_app = APIRouter()

@inv_app.post("/get_item")
async def get_all_Items():
    return await InventoryItem.find_all().to_list()

@inv_app.post("/insert_item")
async def creat_Item(item : InventoryItem):
    await InventoryItem.insert(item)
    return item