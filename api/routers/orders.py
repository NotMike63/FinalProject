from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)

# Create a new Order in the server.
@router.post("/", response_model=schema.Order)
def create(request: schema.OrderBase, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get a specific order from server.
@router.get("/{order_id}", response_model=schema.Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db=db, order_id=order_id)

# Get all orders from the server.
@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get the daily order total in $ from server.
@router.get("/total_price_daily", response_model=float)
def total_price_daily(db: Session = Depends(get_db)):
    return controller.toztal_price_daily(db=db)

# Edits an item in the server.
@router.put("/{order_id}", response_model=schema.OrderUpdate)
def update(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)

# Deletes a specific order based on tracking number.
@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)