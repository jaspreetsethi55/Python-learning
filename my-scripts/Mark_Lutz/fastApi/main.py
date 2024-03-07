# main.py

from fastapi import FastAPI,Request
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item(request: Request,item_id: int):
    print(request.headers)
    return {
            "header'":  request.headers,
            "item_id": item_id
            }


@app.post("/items/")
async def create_item(item: Item):
    print(type(item))
    print(item)
    item_dict = item.dict()
    if int(item.price) > 40:
        item_dict['new_tax'] = 5 
    return item_dict
