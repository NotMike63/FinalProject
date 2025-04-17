from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import RatingsAndReviews as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['RatingsAndReviews'],
    prefix="/RatingsAndReviews"
)

# Create a new Rating and Review in server.
@router.post("/", response_model=schema.RatingsAndReviews)
def create(request: schema.RatingsAndReviews, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Check the status of your Rating and Review.
@router.get("/{tracking_number}", response_model=schema.RatingsAndReviews)
def get_status(tracking_number: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=tracking_number)

# Get all Ratings and Reviews.
@router.get("/", response_model=list[schema.RatingsAndReviews])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Update a Rating and Review.
@router.put("/{tracking_number}", response_model=schema.RatingsAndReviewsUpdate)
def update(tracking_number: int, request: schema.RatingsAndReviews, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=tracking_number)

# remove Rating and Review
@router.delete("/{tracking_number}")
def delete(tracking_number: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=tracking_number)

