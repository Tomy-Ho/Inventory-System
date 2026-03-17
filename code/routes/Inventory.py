from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from DataModels.InventoryData import InventoryItemBase, InventoryItemOut, ItemResponseStatus

inv_app = APIRouter(prefix="/Inventory", tags=["Inventory"])

@inv_app.get("/get_item", response_model=list[InventoryItemOut])
async def get_all_Items():
    return await InventoryItemBase.find_all().to_list()

@inv_app.get("/search_item", response_model=list[InventoryItemOut])
async def get_specific_item(itemname : str):
    result = await InventoryItemBase.find(InventoryItemBase.itemName == itemname).to_list()
    
    if not result:
        raise HTTPException(status_code=404, detail="No item found.")

    return result

@inv_app.post("/insert_item", response_model=InventoryItemOut, status_code=201)
async def creat_Item(item : InventoryItemBase):
    await InventoryItemBase.insert(item)
    return item

@inv_app.delete("/remove_item", response_model=ItemResponseStatus)
async def delete_item(itemid : str):
    find_item = await InventoryItemBase.get(itemid)

    if not find_item:
        raise HTTPException(status_code=404, detail="Item not found.")
    
    await InventoryItemBase.delete(find_item)
    return ItemResponseStatus(status="success", detals="Item deleted = %d" %find_item)

@inv_app.delete("/clear_inventory", response_model=ItemResponseStatus)
async def delete_all():
    deleted = await InventoryItemBase.find_all().delete()
    return ItemResponseStatus(status="success", detals="amount deleted = %s" %deleted.deleted_count)

@inv_app.put("/update_item_value", response_model=ItemResponseStatus)
async def update_value(itemID : str, new_data : InventoryItemBase):
    old_item = await InventoryItemBase.get(itemID)

    if not old_item:
        raise HTTPException(status_code=404, detail="No item found.")
    
    old_item.itemName = new_data.itemName
    old_item.itemID = new_data.itemName
    old_item.amount = new_data.amount
    old_item.price = new_data.price

    await old_item.save()

    return ItemResponseStatus(status="success", detals="Item updated = %s" %old_item)