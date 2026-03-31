from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="My REST API", version="1.0.0")

# TODO: Define your data models using Pydantic
class Item(BaseModel):
    """
    Item model for requests and responses.
    Add your fields here.
    """
    pass


# TODO: Initialize your data storage (can be a list, dictionary, or database)
# items = []


# TODO: Implement GET endpoint to retrieve all items
@app.get("/items")
def get_items():
    """Retrieve all items"""
    pass


# TODO: Implement GET endpoint to retrieve a single item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by ID"""
    pass


# TODO: Implement POST endpoint to create a new item
@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item"""
    pass


# TODO: Implement PUT endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item"""
    pass


# TODO: Implement DELETE endpoint to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
