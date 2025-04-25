from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas import promotions as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['promotions'],
    prefix="/promotions"
)

# Create a new promotion code
@router.post("/", response_model=schema.Promotion)
def create_promo_code(request: schema.PromotionBase, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/{id}", response_model=schema.Promotion)
def read_one(id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, id=id)

@router.get("/", response_model=list[schema.Promotion])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.put("/{id}", response_model=schema.Promotion)
def update(id: int, request: schema.PromotionUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, id=id)

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, id=id)

