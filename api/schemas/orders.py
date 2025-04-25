from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    order_status: bool
    order_date: datetime
    total_price: float
    order_id: int
    customer: str

class OrderCreate(OrderBase):
    order_status: bool
    customer: str
    order_date: datetime
    total_price: float
    order_id: int
    order_detail: Optional[list[OrderDetail]]

class OrderUpdate(BaseModel):
    customer: Optional[str] = None
    total_price: Optional[float] = None
    order_status: Optional[bool] = False



class Order(OrderBase):
    order_id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
