from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
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

@inv_app.put("/update_item_value")
async def update_value(itemID : str, new_data : InventoryItem):
    old_item = await InventoryItem.get(itemID)

    if not old_item:
        raise HTTPException(status_code=404, detail="No item found.")
    
    old_item.itemName = new_data.itemName
    old_item.itemID = new_data.itemName
    old_item.amount = new_data.amount
    old_item.price = new_data.price

    await old_item.save()

    return{
        "status" : "success",
        "Item updated": old_item
    }