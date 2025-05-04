from typing import Optional

from pydantic import BaseModel


class MenuItem(BaseModel):
    name: str
    price: float
    calories: int
    category: str


class MenuItemCreate(MenuItem):
    pass

class MenuItemUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]
    calories: Optional[int]
    category: Optional[str]


class MenuItemOut(MenuItem):
    id: int

