from fastapi import FastAPI
from fastapi import APIRouter
from DataModels.InventoryData import InventoryItem

inv_app = APIRouter()

@inv_app.get("/get_item")
async def get_all_Items():
    return await InventoryItem.find_all().to_list()

@inv_app.post("/insert_item")
async def creat_Item(item : InventoryItem):
    await InventoryItem.insert(item)
    return item

@inv_app.delete("/remove_item")
async def delete_item(item : InventoryItem):
    await InventoryItem.delete(item)
    return item

@inv_app.delete("/clear_inventory")
async def delete_all():
    deleted = await InventoryItem.find_all().delete()
    return {
        "status": "succsess",
        "amount deleted": deleted.deleted_count
        }