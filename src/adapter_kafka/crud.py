import datetime

from sqlalchemy.orm import Session

from sqlalchemy import update, insert

import src.back_list.models

from src.back_list import schemas

from src.back_list.models import Status

def create_record_kafka(db: Session, record: schemas.RecordCreate, user_id: int):
    db_record = src.back_list.models.Record(name=record.name,
                                            url=record.url,
                                            category_id=record.category_id,
                                            created_at=datetime.datetime.now(),
                                            user_id=user_id)
    return db_record