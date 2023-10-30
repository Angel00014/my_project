import datetime

from sqlalchemy.orm import Session

import src.back_list.models

from src.back_list import schemas


# CRUD Категории


def get_category(db: Session, category_id: int):
    return db.query(src.back_list.models.Category).filter(src.back_list.models.Category.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return db.query(src.back_list.models.Category).filter(src.back_list.models.Category.name == category_name).first()


def get_all_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(src.back_list.models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = src.back_list.models.Category(name=category.name, created_at=datetime.datetime.now())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# CRUD Записи

def get_record(db: Session, record_id: int, user_id: int):
    return db.query(src.back_list.models.Record).filter(src.back_list.models.Record.id == record_id and
                                                        src.back_list.models.Record.user_id == user_id).first()


def get_record_by_name(db: Session, record_name: str, user_id: int):
    return db.query(src.back_list.models.Record).filter(src.back_list.models.Record.name == record_name).first()


def get_all_records(db: Session,
                    skip: int = 0,
                    limit: int = 100,
                    user_id: int = None):
    return db.query(src.back_list.models.Record).offset(skip).limit(limit).filter(
        src.back_list.models.Record.user_id == user_id).all()


def create_record(db: Session, record: schemas.RecordCreate, user_id: int):
    db_record = src.back_list.models.Record(name=record.name,
                                            url=record.url,
                                            category_id=record.category_id,
                                            created_at=datetime.datetime.now(),
                                            user_id=user_id)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record
