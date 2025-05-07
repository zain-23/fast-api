from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

# Model
class Item(BaseModel):
    name:str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
def home():
    return {"message":"Hello World"}

@app.post("/items")
def create_item(item:Item):
    item_dic = item.dict()

    if item.tax is not None:
        price_with_tax  = item.price + item.tax
        item_dic.update({ "price_with_tax": price_with_tax})
    return item_dic

@app.put("/items/{item_id}")
def update_item(item_id:str, item:Item, q:Union[str | None]):
    result = {"item_id":item_id, **item.dict(exclude_none=True)}
    if q:
        result.update({"q":q})
    
    return result