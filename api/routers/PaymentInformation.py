from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import order_details as controller
from ..schemas import PaymentInformation as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['PaymentInformation'],
    prefix="/PaymentInformation"
)


@router.post("/{payment_id}", response_model=schema.PaymentStatus)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Check the status of your payment
@router.get("/{payment_id}", response_model=schema.PaymentStatus)
def get_status(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{payment_id}", response_model=schema.OrderDetail)
def update(item_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


# remove payment
@router.delete("/{payment_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
