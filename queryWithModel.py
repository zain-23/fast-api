from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Literal, Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

class FilterParams(BaseModel):
    model_config = {"extra":"forbid"}
    
    limit:int = Field(10, gt=0, le=100)
    offset:int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags:list[str] = []

@app.get("/items")
def get_items(filter_query:Annotated[FilterParams, Query()]):
    return filter_query
