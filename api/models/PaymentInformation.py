from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentInformation(Base):
    __tablename__ = "payment_information"

    card_info = Column(String, primary_key=True)
    transaction_status = Column(BOOLEAN, nullable=False, default=False)
    payment_type = Column(String, nullable=False)

    #sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Payment_Information", back_populates="payment_id")
