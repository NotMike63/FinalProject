
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import DateTime

from .order_details import OrderDetail



class OrderBase(BaseModel):
    tracking_number: int
    order_status: bool
    order_date: datetime
    total_price: float
    customer: str

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    customer_name: Optional[str] = None



class Order(OrderBase):


    class ConfigDict:
        from_attributes = True
