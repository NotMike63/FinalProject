from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from ..models import RatingsAndReviews as model


# This method controls the functionality of creating a new element in the RatingsAndReviews table.
def create(db: Session, request):
    new_item = model.RatingsAndReviews(
        tracking_number=request.tracking_number,
        review_text=request.review_text,
        review_score=request.review_score
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


# This method defines the controls of reading all elements from table in fastapi.
def read_all(db: Session):
    try:
        result = db.query(model.RatingsAndReviews).all()
    except SQLAlchemyError as e:
        #error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Table is empty.")
    return result


def read_one(db: Session, tracking_number):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.tracking_number == tracking_number).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


# This method controls the functionality of updating a single element in the RatingsAndReviews table.
def update(db: Session, tracking_number, request):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.tracking_number == tracking_number)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


# This controls the functionality of deleting an element from the RatingsAndReviews table.
def delete(db: Session, tracking_number):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.tracking_number == tracking_number)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
