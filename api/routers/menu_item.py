from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Menu Items"],
    prefix="/menu-items"
)

@router.post("/", response_model=schema.MenuItemOut, status_code=status.HTTP_200_OK)
def create_menu_item(item: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create_menu_item(db, item)

@router.get("/", response_model=list[schema.MenuItemOut], status_code=status.HTTP_200_OK)
def get_all_menu_items(db: Session = Depends(get_db)):
    return controller.get_all_menu_items(db)

@router.get("/{item_id}", response_model=schema.MenuItemOut, status_code=status.HTTP_200_OK)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.get_menu_item_by_id(db, item_id)

@router.put("/{item_id}", response_model=schema.MenuItemOut, status_code=status.HTTP_200_OK)
def update_menu_item(item_id: int, item: schema.MenuItemUpdate, db: Session = Depends(get_db)):
    return controller.update_menu_item(db, item_id, item)

@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    return controller.delete_menu_item(db, item_id)
