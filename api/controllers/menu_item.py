from typing import Type
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from api.models.menu_item import MenuItem
from ..schemas.menu_item import MenuItemCreate, MenuItemUpdate


def create_menu_item(db: Session, item_data: MenuItemCreate):
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

def get_menu_item_by_id(db: Session, menu_item_id: int):
    item = db.query(MenuItem).get(menu_item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item

def update_menu_item(db:Session, item_id: int, data: MenuItemUpdate):
    item = db.query(MenuItem).filter(MenuItem.id == item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    update_data = data.dict(exclude_unset=True)
    item.update(update_data, synchronize_session=False)
    db.commit()
    return db.query(MenuItem).filter(MenuItem.id == item_id).first()

def delete_menu_item(db:Session, menu_item_id: int):
    item = get_menu_item_by_id(db, menu_item_id)

    try:
        db.delete(item)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return None