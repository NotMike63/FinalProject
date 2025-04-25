from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import RatingsAndReviews as controller
from ..dependencies.database import get_db
from ..schemas import RatingsAndReviews as schema

router = APIRouter(
    tags=['RatingsAndReviews'],
    prefix="/RatingsAndReviews"
)

# Create a new Rating and Review in server.
@router.post("/", response_model=schema.RatingsAndReviews)
def create(request: schema.RatingsAndReviews, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Check the status of your Rating and Review.
@router.get("/{order_id}", response_model=schema.RatingsAndReviews)
def get_status(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)

# Get all Ratings and Reviews.
@router.get("/", response_model=list[schema.RatingsAndReviews])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Update a Rating and Review.
@router.put("/{order_id}", response_model=schema.RatingsAndReviewsUpdate)
def update(order_id: int, request: schema.RatingsAndReviews, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)

# remove Rating and Review
@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)

@router.post("/food-review")
def create_food_review(request: RatingsAndReviews, db: Session = Depends(get_db)):
    return controller.create_food_review(db, request)

@router.get("/popular")
def view_popular_items(db: Session = Depends(get_db)):
    return controller.get_popular_items(db)
