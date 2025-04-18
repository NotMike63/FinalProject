from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BOOLEAN, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class RatingsAndReviews(Base):
    __tablename__ = "RatingsAndReviews"

    tracking_number = Column(Integer, primary_key=True, index=True, autoincrement=True) # ForeignKey("orders.order_id")
    review_text = Column(String(500), nullable=False)
    review_score = Column(Float, nullable=False)