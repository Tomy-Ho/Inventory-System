from pydantic import Field, EmailStr
from beanie import Document

class User(Document):
    name: str
    id: int
    email: EmailStr
    password: str

    class Settings:
        name = "Users"