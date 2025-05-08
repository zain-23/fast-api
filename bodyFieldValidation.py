from typing import Annotated, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Union[str, None] = Field(default=None, title="The description of the item", max_length=300)
    price:float = Field(gt=0, title="The price must be greater than zero")
    tax:Union[float, None] = None

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Annotated[Item, Body(embed=True)]):
    result = {"item_id":item_id, "item":item}
    return result