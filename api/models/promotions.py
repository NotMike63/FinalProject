from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    tracking_number = Column(Integer, ForeignKey("orders.tracking_number"), primary_key=True, index=True)
    code = Column(String(100), unique=True, nullable=True)
    expiration_date = Column(String(100), nullable=True)
