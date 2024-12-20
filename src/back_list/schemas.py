from datetime import datetime

from pydantic import BaseModel

from src.back_list.models import Status


class RecordBase(BaseModel):
    name: str
    url: str


class RecordCreate(RecordBase):
    category_id: int


class Record(RecordBase):
    id: int
    category_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class RecordUpdate(RecordBase):
    id: int
    category_id: int


class RecordDelete(BaseModel):
    pass

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime
    status: Status

    class Config:
        from_attributes = True


class CategoryUpdate(CategoryBase):
    id: int
    status: Status

    class Config:
        from_attributes = True
