from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .PaymentInformation import OrderDetail



class OrderBase(BaseModel):
    tracking_number: int
    order_status: bool
    order_date: datetime
    total_price: float
    customer: str
    # order_details -- relationship
    # description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True
