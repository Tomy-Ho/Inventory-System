from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from DataModels.InventoryData import InventoryItemBase
from DataModels.UserData import UserIn

async def InitializeDB():
    clientConnection = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=clientConnection.inventoryDB, document_models=[InventoryItemBase, UserIn])
