import datetime

import logging

from fastapi import HTTPException
from sqlalchemy.orm import Session

import src.back_list.models

from src.imports.schemas import ImportRecordBase
from src.config import ID_IMPORT_CATEGORY

logging.basicConfig(
    filename='app.log',  # Имя файла для записи логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат сообщений лога
)


def create_import_records(db: Session, imports_records: ImportRecordBase, user_id: int):
    imports_add_records = []
    logging.info(f'Зашли в crud')
    for import_record in imports_records:
        db_record = src.back_list.models.Record(name=import_record['name'],
                                                url=import_record['url'],
                                                category_id=int(ID_IMPORT_CATEGORY),
                                                created_at=datetime.datetime.now(),
                                                user_id=user_id)
        db.add(db_record)
        db.commit()
        db.refresh(db_record)
        imports_add_records.append(import_record)

    if imports_add_records is None:
        raise HTTPException(status_code=400, detail="Ошибка импорта 4")
    else:
        logging.info(f'Зашли выходим из crud {imports_records}')
        return imports_records