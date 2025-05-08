from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Union, Annotated

app = FastAPI()

class Item(BaseModel):
    # Field with example
    # name:str = Field(examples=["Foo"])
    # description:Union[str, None] = Field(default=None, examples=["A very nice item"])
    # price:float = Field(examples=[12.43])
    # tax:Union[float, None] = Field(default=None, examples=[12.3])
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    # Or you can all do this instead
    # model_config = {
    #     "json_schema_extra":{
    #         "examples":[
    #             {
    #                 "name":"Foo",
    #                 "description":"lorem ipsum sre ers oookkd",
    #                 "price":12.3,
    #                 "tax":1.2
    #             }
    #         ]
    #     }
    # }

@app.get("/")
def root():
    return {"message":"Hello world"}

# Body with example
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(examples=[
    {
        "name": "Foo",
        "description": "A very nice Item",
        "price": 35.4,
        "tax": 3.2,
    }
])]):
    results = {"item_id": item_id, "item": item}
    return results