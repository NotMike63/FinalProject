from typing import Optional

from pydantic import BaseModel



class PromotionBase(BaseModel):
    code: str
    expiration_date: str
    is_active: bool = True

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    expiration_date: Optional[str] = None
    is_active: Optional[bool] = None


class Promotion(PromotionBase):
    id: int

    class ConfigDict:
        from_attributes = True
