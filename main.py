from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def main_page():
    return {"Hello": "World"}


@app.get("items/{item_id}")
def items_page(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.price, "item_id": item_id}
