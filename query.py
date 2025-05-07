from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/items")
def read_items(skip:int = 0, limit:int = 10):
    return fake_items_db[skip:skip + limit]

@app.get("/items/{item_id}")
def read_item(item_id:str, q:Union[str, None] = None, short:bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"})

    return item

@app.get("/users/{user_id}/items/{item_id}")
def read_user(user_id:str, item_id:str, q:Union[str,None] = None, short:bool = False):
    item = {"user_id":user_id, "item_id":item_id}

    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"})
    
    return item
