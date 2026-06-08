"""
Starter code for the FastAPI REST API assignment.

Run locally:
    pip install -r assignments/fastapi-rest-api/requirements.txt
    python assignments/fastapi-rest-api/starter-code.py

This file provides a minimal in-memory CRUD API for `Item` resources.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from uuid import uuid4


app = FastAPI(title="FastAPI Assignment - Items API")


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., ge=0)


class Item(ItemBase):
    id: str


# Simple in-memory store: id -> Item
_items: Dict[str, Item] = {}


@app.get("/items", response_model=List[Item])
def list_items():
    return list(_items.values())


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: ItemBase):
    item_id = str(uuid4())
    new_item = Item(id=item_id, **item.dict())
    _items[item_id] = new_item
    return new_item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: str, item: ItemBase):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **item.dict())
    _items[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return None


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
