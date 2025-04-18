from sqlalchemy import Column, Integer, String

from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False,)
    address = Column(String(255), nullable=False)