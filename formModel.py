from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello world"}

class FormData(BaseModel):
    username:str
    password:str
    model_config = {"extra": "forbid"}

@app.post("/login")
def login(data:Annotated[FormData, Form()]):
    return data