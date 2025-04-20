from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..controllers import customer as controller
from ..schemas import customer as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=["Customers"],
    prefix="/customers"
)

@router.post("/", response_model=schema.CustomerOut)
def create_customer(customer: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create_customer(db, customer)

@router.get("/", response_model=list[schema.CustomerOut])
def get_all_customers(db: Session = Depends(get_db)):
    return controller.get_all_customers(db)

@router.get("/{customer_id}", response_model=schema.CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.get_customer(db, customer_id)

@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete_customer(db, customer_id)
