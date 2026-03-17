from pydantic import Field, EmailStr, field_validator, BaseModel
from beanie import Document

class UserBase(Document):
    name: str
    age: int = Field(ge=0)
    email: EmailStr = Field(examples=['example123@mail.com'])

    class Settings:
        name = "Users"

class UserIn(UserBase):
    password: str = Field(min_length=8)

    @field_validator('password')
    @classmethod
    def checkPassword(cls, passwordtocheck: str):
            if not any (char.isupper() for char in passwordtocheck):
                raise ValueError("Password must include at least one upper letter.")
            if not any (char.islower() for char in passwordtocheck):
                raise ValueError("Password must include at least one lower letter.")
            if not any (char.isdigit() for char in passwordtocheck):
                raise ValueError("Password must include at least one number.")
            if not any (char.isalnum() for char in passwordtocheck):
                raise ValueError("Password must include at least one special character.")
            return passwordtocheck

class UserOut(UserBase):
     pass

class UserResponseStatus(BaseModel):
    status: str
    details: str