from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    tracking_number: int
    order_status: bool
    order_date: datetime
    total_price: float
    customer: str

class OrderCreate(OrderBase):
    tracking_number: int
    order_status: bool

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True