from pydantic import Field
from beanie import Document

class InventoryItem(Document):
    itemName: str
    itemID: int
    amount: int
    price: float

    class Settings:
        name = "Items"