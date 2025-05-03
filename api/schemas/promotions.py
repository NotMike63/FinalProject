from typing import Optional

from pydantic import BaseModel



class PromotionBase(BaseModel):
    code: str
    expiration_date: str
    is_active: bool = True
    discount_type: str
    discount_value: float


class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    expiration_date: Optional[str] = None
    is_active: Optional[bool] = None
    discount_type: Optional[str] = None
    discount_value: Optional[float] = None


class Promotion(PromotionBase):
    id: int

    #class ConfigDict:
        #from_attributes = True
