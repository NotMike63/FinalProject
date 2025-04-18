from pydantic import BaseModel

from .orders import Order


class PromotionBase(BaseModel):
    tracking_number: int
    code: str
    expiration_date: str


class Promotion(PromotionBase):
    order: Order = None

    class ConfigDict:
        from_attributes = True
