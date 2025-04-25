from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import promotions as model
from sqlalchemy.exc import SQLAlchemyError

def create(db: Session, request):
    new_promotion = model.Promotion(
        code=request.code,
        expiration_date=request.expiration_date,
        is_active = request.is_active
    )

    db.add(new_promotion)
    db.commit()
    db.refresh(new_promotion)
    return new_promotion


def read_all(db: Session):
    result = db.query(model.Promotion).all()
    return result


def read_one(db: Session, id: int):
    promotion = db.query(model.Promotion).filter(
        model.Promotion.id == id
    ).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


def update(db: Session, request, id: int):
    promotion = db.query(model.Promotion).filter(
        model.Promotion.id == id
    )
    if not promotion.first():
        raise HTTPException(status_code=404, detail="Promotion not found")
    update_data = request.dict(exclude_unset=True)
    promotion.update(update_data, synchronize_session=False)
    db.commit()
    return promotion.first()


def delete(db: Session, id: int):
    promotion = db.query(model.Promotion).filter(
        model.Promotion.id == id
    )
    if not promotion.first():
        raise HTTPException(status_code=404, detail="Promotion not found")
    promotion.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)