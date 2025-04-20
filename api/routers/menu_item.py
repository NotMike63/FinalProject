from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import menu_item as controller
from ..schemas import menu_item as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Menu Items"],
    prefix="/menu-items"
)

@router.post("/", response_model=schema.MenuItemOut)
def create_menu_item(item: schema.MenuItemCreate, db: Session = Depends(get_db)):
    return controller.create_menu_item(db, item)

@router.get("/", response_model=list[schema.MenuItemOut])
def get_all_menu_items(db: Session = Depends(get_db)):
    return controller.get_all_menu_items(db)