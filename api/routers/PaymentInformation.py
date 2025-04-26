from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers import PaymentInformation as controller
from ..dependencies.database import get_db
from ..schemas import PaymentInformation as schema

router = APIRouter(
    tags=['PaymentInformation'],
    prefix="/PaymentInformation"
)

# Create a new PaymentInformation in server.
@router.post("/", response_model=schema.PaymentInformation)
def create(request: schema.PaymentInformation, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

# Check the status of your payment.
@router.get("/{payment_id}", response_model=schema.PaymentInformation)
def get_status(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=payment_id)

# Get a single PaymentInformation
@router.get("/{payment_id}", response_model=schema.PaymentInformation)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)

# Get all payment information.
@router.get("/", response_model=list[schema.PaymentInformation])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Update a payment information.
@router.put("/{payment_id}", response_model=schema.PaymentInformation)
def update(order_id: int, request: schema.PaymentInformationUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, order_id=order_id, request=request)

# remove payment
@router.delete("/{payment_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)
