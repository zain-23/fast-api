from fastapi import FastAPI, Query, Path
from typing import Union, Annotated
from pydantic import AfterValidator

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World"}

# Path Parameters and Numeric Validations

@app.get("/items/{item_id}")
def get_item(item_id:Annotated[int, Path(title="The ID of the item to get", gt=10)], q:Annotated[Union[str, None],Query(alias="item-query")] = None):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result