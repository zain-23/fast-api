from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from pydantic import BaseModel
from typing import Union

fake_db = {}

app = FastAPI()

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None

@app.put("/items/{item_id}")
def update_item(item_id:str, item:Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[item_id] = json_compatible_item_data
    return item

@app.get("/items")
def get_items():
    return fake_db