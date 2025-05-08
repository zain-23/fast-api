from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/item", status_code=status.HTTP_201_CREATED)
def create_item(item:Item):
    return {**item.model_dump()}
