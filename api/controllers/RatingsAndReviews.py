from fastapi import HTTPException, status, Response
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ..models import RatingsAndReviews as model
from ..models.orders import Order


# This method controls the functionality of creating a new element in the RatingsAndReviews table.
def create(db: Session, request):
    order = db.query(Order).filter(Order.order_id == request.order_id).first()
    if not order:
        raise HTTPException(status_code=400, detail=f"Order ID {request.order_id} does not exist.")

    new_item = model.RatingsAndReviews(
        order_id=request.order_id,
        review_text=request.review_text,
        review_score=request.review_score,
        customer_name=request.customer_name
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
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, order_id):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.order_id == order_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


# This method controls the functionality of updating a single element in the RatingsAndReviews table.
def update(db: Session, order_id, request):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.order_id == order_id)
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
def delete(db: Session, order_id):
    try:
        item = db.query(model.RatingsAndReviews).filter(model.RatingsAndReviews.order_id == order_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)