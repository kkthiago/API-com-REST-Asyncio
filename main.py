from fastapi import FastAPI
from pydantic import BaseModel, Field
import uuid
import asyncio

app = FastAPI()
items = []

class Item(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    item: str
    
    
@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": "Welcome to the API"}

@app.post("/items")
async def create_item(item: Item):
    await asyncio.sleep(0.1)
    items.append(item)
    return item


@app.put("/items/{id}")
async def update_item(id: int, item: str):
    await asyncio.sleep(0.1)
    if 0 <= id < len(items):
        items[id] = item
        return {"message": "Item updated", "item": item}
    else:
        return {"message": "Item not found"}, 404

@app.delete("/items/{id}")
async def delete_item(id: int):
    await asyncio.sleep(0.1)
    if 0 <= id:
        deleted_item = items.pop(id)
        return {"message": "Item deleted", "item": deleted_item}
    else:
        return {"message": "Item not found"}, 404

