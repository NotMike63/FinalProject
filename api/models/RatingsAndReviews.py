from sqlalchemy import Column, ForeignKey, Integer, String, Float

from ..dependencies.database import Base


class RatingsAndReviews(Base):
    __tablename__ = "RatingsAndReviews"
    menu_item_id = Column(Integer, ForeignKey("menu_items.menu_item_id"), nullable=False)
    order_id = Column(Integer, ForeignKey("orders.order_id"), primary_key=True, index=True, autoincrement=True)
    review_text = Column(String(500), nullable=False)
    review_score = Column(Float, nullable=False)