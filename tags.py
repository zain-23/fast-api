from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()

class Tags(Enum):
    item = "Item"
    user = "User"

@app.get("/items", tags=[Tags.item])
def get_item():
    return [{"item": "Foo", "price": 42}]