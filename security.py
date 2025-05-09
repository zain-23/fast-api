from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items")
def read_items(token:Annotated[str, Depends(oauth_scheme)]):
    return token
