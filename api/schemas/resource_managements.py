from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ResourceManagementBase(BaseModel):
    items: str
    amount: int
    resource_management_id: int


class ResourceManagementCreate(ResourceManagementBase):
    resource_management_id: int


class ResourceManagementUpdate(BaseModel):
    items: Optional[str] = None
    amount: Optional[int] = None
    resource_management_id: int


class ResourceManagement(ResourceManagementBase):
    resource_management_id: int
    '''class ConfigDict:
            from_attributes = True'''

    class Config:
        orm_mode = True


