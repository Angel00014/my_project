import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now())

    # record = relationship("Record", back_populates="category")
    # record = relationship("Record", foreign_keys=[category_id])


class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.now())
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", foreign_keys=[category_id])