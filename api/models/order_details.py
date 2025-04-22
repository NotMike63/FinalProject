from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True, index=True)
    amount = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="order_details", foreign_keys=[order_id])