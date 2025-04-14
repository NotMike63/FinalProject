from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime, BOOLEAN, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, ForeignKey("order_details.order_id"), primary_key=True, autoincrement=True)
    tracking_number = Column(Integer, unique=True)
    order_status = Column(BOOLEAN, nullable=False, default=False)
    order_date = Column(DateTime, nullable=False, server_default=str(datetime.now()))
    total_price = Column(Float, nullable=False, default=0.00)
    customer = Column(String(100), nullable=False)

    order_details = relationship("OrderDetail", back_populates="order")