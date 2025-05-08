from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app = FastAPI()

# class UserIn(BaseModel):
#     username:str
#     password:str
#     email:EmailStr
#     full_name:Union[str, None] = None

# class UserOut(BaseModel):
#     username:str
#     email:EmailStr
#     full_name:Union[str, None] = None

# class UserInDB(BaseModel):
#     username:str
#     hash_password:str
#     email:EmailStr
#     full_name:Union[str, None] = None

class UserBase(BaseModel):
    username:str
    full_name:str
    email:EmailStr

class UserIn(UserBase):
    password:str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hash_password:str

def fake_password_hasher(password:str):
    return "supersecret" + password

def fake_user_db(user_in:UserIn):
    hash_password = fake_password_hasher(user_in.password)
    save_user = UserInDB(**user_in.model_dump(),hash_password=hash_password)
    print("User saved! ..not really")
    return save_user


@app.post("/user", response_model=UserOut)
def create_user(user:UserIn):
    save_user = fake_user_db(user)
    return save_user

# Declare response to be union

class BaseItem(BaseModel):
    description:str
    type:str

class CarItem(BaseItem):
    type:str = "car" 

class PlaneItem(BaseItem):
    type:str = "plane"
    size:int

items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@app.get("/items/{item_id}", response_model=Union[CarItem, PlaneItem])
def get_item(item_id:str):
    return items[item_id]