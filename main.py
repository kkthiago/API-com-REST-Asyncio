from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid
import asyncio

app = FastAPI()
items = []

class Item(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str

@app.get("/")
async def root():
    await asyncio.sleep(0.1)
    return {"message": "Welcome to the FastAPI application!"}
    
@app.post("/items")
async def create_item(item: Item, ):
    await asyncio.sleep(0.1)
    if not item.name or not item.name.strip():
        raise HTTPException(status_code=400, detail="Item name cannot be empty")
    item.name = item.name.capitalize()
    items.append(item)
    return {"message": "The following item was created successfully:", "item": item}
 
@app.get("/items")
async def list_items():
    await asyncio.sleep(0.1)
    if not items:
        raise HTTPException(status_code=404, detail="No items were registered yet, Try creating an item first")   
    return {"message": "List of items:", "item": items}

@app.put("/items/{item_id}")
async def update_item(item_id: uuid.UUID, updated_item: Item):
    await asyncio.sleep(0.1)
    if not items:
        raise HTTPException(status_code=404, detail="No items were registered yet, Try creating an item first") 
    for item in items:
        if item.id == item_id:
            item.name = updated_item.name.capitalize()
            return {"message": "The following item was updated successfully:", "item": item}
            
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: uuid.UUID):
    await asyncio.sleep(0.1)
    for idx, item in enumerate(items):
        if item.id == item_id:
            deleted_item = items.pop(idx)
            return {"message": "Item deleted successfully:","item": deleted_item}
    raise HTTPException(status_code=404, detail="Item not found")
    