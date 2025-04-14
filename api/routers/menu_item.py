from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.menu_item import MenuItem
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Menu Items"],
    prefix="/menu-items"
)

@router.post("/", response_model=schema.MenuItemOut)
def create_menu_item(item: schema.MenuItemCreate, db: Session = Depends(get_db)):
    db_item = MenuItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=list[schema.MenuItemOut])
def get_all_menu_items(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()
