from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from DataModels.InventoryData import InventoryItem
from DataModels.UserData import User

async def InitializeDB():
    clientConnection = AsyncIOMotorClient("mongodb://localhost:27017/test")
    await init_beanie(database=clientConnection.inventoryDB, document_models=[InventoryItem, User])
