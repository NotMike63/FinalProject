from typing import Type
from fastapi import HTTPException, status, Response, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from api.models.menu_item import MenuItem
from ..schemas.menu_item import MenuItemCreate

def create_menu_item(db: Session, item_data: MenuItemCreate) -> MenuItem:
    menu_item = MenuItem(**item_data.dict())
    try:
        db.add(menu_item)
        db.commit()
        db.refresh(menu_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return menu_item

def get_all_menu_items(db: Session) -> list[Type[MenuItem]]:
    try:
        results = db.query(MenuItem).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return results
