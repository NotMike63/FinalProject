from sqlalchemy import Column, ForeignKey, Integer, String

from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"

    code = Column(String(100), unique=True, nullable=True, primary_key=True)
    expiration_date = Column(String(100), nullable=True)

