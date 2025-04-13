from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import PaymentInformation as controller
from ..schemas import PaymentInformation as schema
from ..dependencies.database import engine, get_db

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
    return controller.read_one(db, card_info=payment_id)

# Get all payment information.
@router.get("/", response_model=list[schema.PaymentInformation])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

# Update a payment information.
@router.put("/{payment_id}", response_model=schema.PaymentInformation)
def update(payment_id: int, request: schema.PaymentInformationUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, card_info=payment_id)

# remove payment
@router.delete("/{payment_id}")
def delete(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, card_info=payment_id)
