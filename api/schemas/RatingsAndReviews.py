from pydantic import BaseModel

class RatingsAndReviews(BaseModel):
    review_text: str
    order_id: int
    review_score: float
    customer_name: str

    class Config:
        orm_mode = True

class RatingsAndReviewsUpdate(BaseModel):
    review_text: str
    review_score: float

