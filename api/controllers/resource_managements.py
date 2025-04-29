from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import resource_managements as model
from sqlalchemy.exc import SQLAlchemyError

from ..schemas import resource_managements
from api.schemas import resource_managements


def create(db: Session, request):
    new_items = model.ResourceManagement(
        items=request.items,
        amount=request.amount,
        resource_management_id=request.resource_management_id
    )

    try:
        db.add(new_items)
        db.commit()
        db.refresh(new_items)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_items


def read_all(db: Session):
    try:
        results = db.query(model.ResourceManagement).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return results


def read_one(db: Session, resource_management_id):
    items = db.query(model.ResourceManagement).filter(model.ResourceManagement.resource_management_id == resource_management_id).first()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    return items


def update(db: Session, resource_management_id: int, request):
    try:
        items = db.query(model.ResourceManagement).filter(
            model.ResourceManagement.resource_management_id == resource_management_id
        ).first()

        print(items.__dict__)

        if not items:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")

        items.amount = request.amount
        items.items = request.items

        db.commit()
        #db.refresh(items)
        #return {"message": "Resource management record updated successfully"}

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def delete(db: Session, resource_management_id):
    try:
        items = db.query(model.ResourceManagement).filter(
            model.ResourceManagement.resource_management_id == resource_management_id
        )
        if not items.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        items.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
