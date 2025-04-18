from pydantic import BaseModel

class RatingsAndReviews(BaseModel):
    tracking_number: int
    review_text: str
    review_score: float
    customer_name: str

class RatingsAndReviewsUpdate(BaseModel):
    tracking_number: int
    new_review_text: str
    new_review_score: float
