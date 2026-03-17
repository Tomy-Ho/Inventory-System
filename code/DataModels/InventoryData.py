from pydantic import Field, BaseModel
from beanie import Document

class InventoryItemBase(Document):
    itemName: str
    itemID: int
    amount: int = Field(ge=0, default=0)
    price: float = Field(ge=0, default=0)

    class Settings:
        name = "Items"

class InventoryItemOut(InventoryItemBase):
    pass

class ItemResponseStatus(BaseModel):
    status: str
    detals: str