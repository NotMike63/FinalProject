from typing import Optional

from pydantic import BaseModel


class ResourceManagementBase(BaseModel):
    item: str
    amount: int


class ResourceManagementCreate(ResourceManagementBase):
    pass


class ResourceManagementUpdate(BaseModel):
    item: Optional[str] = None
    amount: Optional[int] = None


class ResourceManagement(ResourceManagementBase):
    id: int

    class ConfigDict:
        from_attributes = True