import datetime

from sqlalchemy.orm import Session

from sqlalchemy import update, insert

import src.back_list.models

from src.back_list import schemas

from src.back_list.models import Status


# CRUD Категории


def get_category(db: Session, category_id: int):
    return db.query(src.back_list.models.Category).filter(src.back_list.models.Category.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return db.query(src.back_list.models.Category).filter(src.back_list.models.Category.name == category_name).first()


def get_all_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(src.back_list.models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = src.back_list.models.Category(name=category.name, created_at=datetime.datetime.now(),
                                                status=Status.active)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category: schemas.CategoryUpdate):
    db_category = db.query(src.back_list.models.Category).filter(
        src.back_list.models.Category.id == category.id).first()
    db_category.name = category.name
    db_category.status = category.status
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


def update_record(db: Session, record: schemas.RecordUpdate):
    db_record = db.query(src.back_list.models.Record).filter(src.back_list.models.Record.id == record.id).first()
    db_record.name = record.name
    db_record.url = record.url
    db_record.category_id = record.category_id
    db.commit()
    db.refresh(db_record)
    return db_record


def delete_record(db: Session, record_id: int):
    db.query(src.back_list.models.Record).filter(src.back_list.models.Record.id == record_id).delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
