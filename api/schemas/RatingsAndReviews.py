from pydantic import BaseModel

class RatingsAndReviews(BaseModel):
    review_text: str
    order_id: int
    review_score: float
    customer_name: str

    class Config:
        orm_mode = True

class RatingsAndReviewsUpdate(BaseModel):
    new_review_text: str
    new_review_score: float

