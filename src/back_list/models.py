import datetime
import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Enum
from sqlalchemy.orm import relationship

from src.database import Base


class Status(enum.Enum):
    active = '1'
    enabled = '0'


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Enum(Status))
    created_at = Column(TIMESTAMP, default=datetime.datetime.now())


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now())
    category_id = Column(Integer, ForeignKey("category.id"))
    user_id = Column(Integer, ForeignKey("user.id"))

    category = relationship("Category", foreign_keys=[category_id])
    user = relationship("User", foreign_keys=[user_id])
