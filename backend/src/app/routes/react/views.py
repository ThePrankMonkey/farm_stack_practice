from typing import Annotated
from pydantic import BaseModel
from fastapi import APIRouter
from app.db import client

collection = client.test.items

router = APIRouter(
    prefix="/r",
)

class Item(BaseModel):
    item_id: int
    name: str
    price: float
    description: str | None = None

fake_db = {
    1: Item(item_id=1, name="fart", price=1),
    2: Item(item_id=2, name="poop", price=2),
}

sections = [
    { "title": "home", "url": "http://localhost:8000/h/nav/home"},
    { "title": "about", "url": "http://localhost:8000/h/nav/about"},
]

@router.get("/")
async def react_root():
    return {"hello": "world"}

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    result = collection.find_one({"item_id": item_id})
    print(f"Real DB: {result}")
    return Item(**result)

@router.post("/items")
async def make_item(item: Item):
    result = collection.insert_one(item.model_dump())
    print(result)
    return item
