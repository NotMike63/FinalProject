from __future__ import annotations

import sqlalchemy
from fastapi import HTTPException, status, Response, Depends
from http.client import HTTPException
from typing import Type

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from ..models.customer import Customer
from ..schemas.customer import CustomerCreate

def create_customer(db: Session, data: CustomerCreate) -> Customer:
    new = Customer(**data.dict())
    try:
        db.add(new)
        db.commit()
        db.refresh(new)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

    return new

def get_all_customers(db: Session) -> list[Type[Customer]]:
    try:
        return db.query(Customer).all()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_customer(db: Session, customer_id: int) -> Customer | None:
    try:
        return db.query(Customer).filter(Customer.id == customer_id).first()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def delete_customer(db: Session, customer_id: int):
    try:
        customer = get_customer(db, customer_id)
        if not customer:
            raise HTTPException(status_code=404, detail="Customer not found")
        db.delete(customer)
        db.commit()
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=404, detail="Failed to delete customer")
