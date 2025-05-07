# from typing import Union
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name:str
#     price:float
#     is_offer:Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello":"World"}

# @app.get("/items/{item_id}")
# def reat_item(item_id:int, q:Union[str, None] = None):
#     return {"item_id":item_id, "q":q}

# @app.put("/items/{item_id}")
# def update_item(item_id:int, item:Item):
#     return {"item_id":item_id, "price":item.price}

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/user/me")
def read_user_me():
    return {"name":"Syed Zain Ali Shah"}

@app.get("/user/{user_id}")
def get_user_by_id(user_id:str):
    return {"id":user_id}

@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
    
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}        

@app.get("/files/{file_path:path}")
def read_file(file_path:str):
    return {"file_path":file_path}
