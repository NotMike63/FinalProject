from sqlalchemy import Column, ForeignKey, Integer, String, Float

from ..dependencies.database import Base


class RatingsAndReviews(Base):
    __tablename__ = "RatingsAndReviews"
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(500), nullable=False)
    review_score = Column(Float, nullable=False)
    customer_name = Column(String(100), nullable=False)