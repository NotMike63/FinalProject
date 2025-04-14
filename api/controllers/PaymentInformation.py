from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import PaymentInformation as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.PaymentInformation(
        card_info=request.card_info,
        transaction_status=request.transaction_status,
        payment_type=request.payment_type,
        tracking_number=request.tracking_number
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


# This method reads all the items from table.
def read_all(db: Session):
    try:
        result = db.query(model.PaymentInformation).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Table is empty.")
    return result


def read_one(db: Session, card_info):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_info == card_info).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The table is empty.")
    return item

# Update all elements in an item in the table.
def update(db: Session, card_info, request):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_info == card_info)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, card_info):
    try:
        item = db.query(model.PaymentInformation).filter(model.PaymentInformation.card_info == card_info)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
