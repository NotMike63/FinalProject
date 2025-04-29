from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class ResourceManagement(Base):
    __tablename__ = "resource_managements"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    items = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

