from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Union

app = FastAPI()

# class Item(BaseModel):
#     name:str
#     description:Union[str, None]
#     price:float
#     tax:Union[float, None] = None
#     tags:set[str] = set()

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# Nested Model
class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description:Union[str, None]
    price:float
    tax:Union[float, None] = None
    tags:set[str] = set()
    image:Union[Image, None] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
