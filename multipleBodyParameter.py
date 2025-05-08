from typing import Annotated, Union
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Union[str, None]
    price:float
    tax:Union[float, None]

@app.post("/items/{item_id}")
def update_item(
        item_id:Annotated[int, Path(title="The ID of the item to get")],
        q:Union[str, None] = None,
        item:Union[Item, None] = None
        ):
   result = {"item_id", item_id}

   if q:
       result.update({"q": q})
   if item:
       result.update({"item", item})
   return result
       


