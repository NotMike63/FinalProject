from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RatingsAndReviews(BaseModel):
    tracking_number: int
    review_text: str
    review_score: float
