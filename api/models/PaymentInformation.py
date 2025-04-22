from sqlalchemy import Column, ForeignKey, Integer, String, BOOLEAN

from ..dependencies.database import Base


class PaymentInformation(Base):
    __tablename__ = "payment_information"

    card_info = Column(String(100), primary_key=True, nullable=False)
    transaction_status = Column(BOOLEAN, nullable=False, default=False)
    payment_type = Column(String(30), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)

    # sandwich = relationship("Sandwich", back_populates="order_details")
    # payment = relationship("Payment_Information", back_populates="payment_id")
