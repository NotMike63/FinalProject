from typing import Optional
from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel


# Base return
class PaymentInformation(BaseModel):
    card_info: str
    transaction_status: bool
    payment_type: str
    order_id: int

class PaymentRequest(BaseModel):
    card_information: str

# Schema for updating PaymentInformation
class PaymentInformationUpdate(BaseModel):
    card_info: Optional[str] = None
    transaction_status: Optional[bool] = None
    payment_type: Optional[str] = None

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