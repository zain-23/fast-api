from fastapi import FastAPI, Query
from typing import Union, Annotated
from pydantic import AfterValidator
import random
# We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.
# Import Query and Annotated
app = FastAPI()

@app.get("/items")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50, pattern="^Zain$")] = "Zain"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Multiple query parameters
@app.get("/users")
async def read_items(q: Annotated[Union[list[str], None], Query()]):
    query = {"q":q}
    return query

# Alias parameters
# Imagine that you want the parameter to be item-query.
@app.get("/employees")
async def get_employees(q: Annotated[Union[str, None], Query(alias="employee-name", deprecated=True)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Custom validation function
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id:str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get("/movies")
def get_movies(id:Annotated[Union[str, None],AfterValidator(check_valid_id)] = None):
    if id:
        item = data.get(id)
    else:
      id, item = random.choice(list(data.items()))
    return {"id":id, "name": item}
