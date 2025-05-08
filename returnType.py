from typing import Annotated, Union
from fastapi import Cookie, FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# class Item(BaseModel):
#     name:str
#     description:Union[str, None] = None
#     price:float
#     tax:Union[float, None] = None
#     tags:list[str] = []

# @app.get("/items")
# def read_items() -> list[Item]:
#     return [
#         Item(name="Zain", price=12.2),
#         Item(name="Umar", price=13.2)
#     ]

# Response model return type
# class UserIn(BaseModel):
#     username:str
#     password:str
#     email:EmailStr
#     full_name:Union[str, None] = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None

# Don't do this in production!
# @app.post("/user", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user")
async def create_user(user: UserIn) -> BaseUser:
    return user