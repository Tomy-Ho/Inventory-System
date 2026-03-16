from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from DataModels.InventoryData import InventoryItemBase, InventoryItemOut

inv_app = APIRouter()

@inv_app.get("/get_item", response_model=list[InventoryItemOut])
async def get_all_Items():
    return await InventoryItemBase.find_all().to_list()

@inv_app.get("/search_item", response_model=list[InventoryItemOut])
async def get_specific_item(itemname : str):
    result = await InventoryItemBase.find(InventoryItemBase.itemName == itemname).to_list()
    return result

@inv_app.post("/insert_item", response_model=InventoryItemOut)
async def creat_Item(item : InventoryItemBase):
    await InventoryItemBase.insert(item)
    return item

@inv_app.delete("/remove_item")
async def delete_item(item : InventoryItemBase):
    await InventoryItemBase.delete(item)
    return {
        "status" : "success",
        "Item removed" : item
    }

@inv_app.delete("/clear_inventory")
async def delete_all():
    deleted = await InventoryItemBase.find_all().delete()
    return {
        "status": "success",
        "amount deleted": deleted.deleted_count
        }

@inv_app.put("/update_item_value")
async def update_value(itemID : str, new_data : InventoryItemBase):
    old_item = await InventoryItemBase.get(itemID)

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