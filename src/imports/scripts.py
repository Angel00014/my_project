import json
import os
import logging

from fastapi import Depends, HTTPException, APIRouter
from fastapi_users import FastAPIUsers

from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.config import IMPORT_RECORDS_SYSTEM_ONE_MOCK

from src.database import SessionLocal
from src.auth.models import User

from src.imports import crud, schemas
from sqlalchemy.orm import Session

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

logging.basicConfig(
    filename='app.log',  # Имя файла для записи логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат сообщений лога
)


import_router = APIRouter(
    prefix="/back-list/imports/another_system",
    tags=["Import_systems"]
)


@import_router.get("/system_one", response_model=schemas.ImportRecordBase)
def import_record(db: Session = Depends(get_db), user: User = Depends(current_user)):
    check = bool(IMPORT_RECORDS_SYSTEM_ONE_MOCK)
    if check is True:
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_dir = os.path.dirname(os.path.dirname(script_dir))
            file_path = os.path.join(project_dir, "mock", "mock.json")

            with open(file_path, 'r') as file:
                mocks = json.load(file)
            for mock in mocks:
                if (mock['url'] == "/back-list/imports/another_system/system_one") and (mock.get('data')):
                    imports_records = mock['data']
            if imports_records is None:
                raise HTTPException(status_code=404, detail="Мок не найден")
            else:
                if imports_records is not None:
                    import_records_result = crud.create_import_records(db=db,
                                                                       imports_records=imports_records,
                                                                       user_id=user.id)
                    logging.info(f'Итог {type(import_records_result)}')
                    return import_records_result
                else:
                    raise HTTPException(status_code=400, detail="Ошибка импорта 3")
        except:
            raise HTTPException(status_code=400, detail="Ошибка импорта")

    else:
        raise HTTPException(status_code=400, detail="Мок выключен")
