from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)

# Create a new item in table.
@router.post("/", response_model=schema.OrderDetailBase)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Get all items in table.
@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Get specific item from table
@router.get("/{item_id}", response_model=schema.OrderDetailBase)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

# Edit a specific element in table.
@router.put("/{item_id}", response_model=schema.OrderDetailBase)
def update(item_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

# Remove a specified item from table.
@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)