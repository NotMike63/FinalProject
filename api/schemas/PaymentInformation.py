from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import String

from .sandwiches import Sandwich


class PaymentInformation(BaseModel):
    card_info: str
    transaction_status: bool
    payment_type: str

class PaymentStatus(BaseModel):
    card_info: str
    payment_status: bool


# class OrderDetailCreate(OrderDetailBase):
#     order_id: int
#     sandwich_id: int
#
# class OrderDetailUpdate(BaseModel):
#     order_id: Optional[int] = None
#     sandwich_id: Optional[int] = None
#     amount: Optional[int] = None
#
#
# class OrderDetail(OrderDetailBase):
#     id: int
#     order_id: int
#     sandwich: Sandwich = None
#
#     class ConfigDict:
#         from_attributes = True