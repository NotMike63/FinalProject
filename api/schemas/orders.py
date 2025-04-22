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
    customer: Optional[str] = None
    total_price: Optional[float] = None
    order_status: Optional[bool] = False
    order_details: Optional[OrderDetail] = None



class Order(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    tracking_number: int

    class ConfigDict:
        from_attributes = True