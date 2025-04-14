from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]

class CustomerOut(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True