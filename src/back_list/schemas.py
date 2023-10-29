from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

import uuid

from fastapi_users import schemas


class RecordBase(BaseModel):
    name: str
    url: str


class RecordCreate(RecordBase):
    category_id: int
    pass


class Record(RecordBase):
    id: int
    category_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
