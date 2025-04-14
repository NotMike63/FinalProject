from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    tracking_number = Column(Integer, ForeignKey("orders.tracking_number"))
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True, index=True)
    amount = Column(Integer, index=True, nullable=False)

    order = relationship("Order", back_populates="order_details")