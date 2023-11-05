from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi_users import FastAPIUsers

import src
from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
# from fastapi_users import FastAPIUsers
#
# from src.auth.auth import auth_backend
# from src.auth.manager import get_user_manager
from src.database import engine, SessionLocal, Base
from src.auth.models import User
# from src.auth.schemas import UserRead, UserCreate
from src.back_list import crud, schemas
from sqlalchemy.orm import Session

# Base.metadata.create_all(bind=engine)

# app = FastAPI(
#     title="My BackList"
# )

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


category_router = APIRouter(
    prefix="/back-list",
    tags=["Category"])

record_router = APIRouter(
    prefix="/back-list",
    tags=["Record"])


###############################################Категории####################################3########################

@category_router.post("/category", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db),
                    user: User = Depends(current_user)):
    db_category = crud.get_category_by_name(db, category_name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Категория существует! Переименуйте свою категорию.")
    return crud.create_category(db=db, category=category)


@category_router.get("/category", response_model=list[schemas.Category])
def read_all_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                      user: User = Depends(current_user)):
    category = crud.get_all_category(db, skip=skip, limit=limit)
    return category


@category_router.get("/category/{category_id}", response_model=schemas.Category)
def read_one_category(category_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена.")
    return db_category


@category_router.patch("/category", response_model=schemas.Category)
def update_category(category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена.")
    return db_category

# @category_router.options()

###############################################Записи####################################3########################


@record_router.post("/record", response_model=schemas.Record)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    db_record = crud.get_record_by_name(db, record_name=record.name, user_id=user.id)
    if db_record:
        raise HTTPException(status_code=400, detail="Наименование уже существует! Выберете другое наименование")
    return crud.create_record(db=db, record=record, user_id=user.id)


@record_router.get("/record", response_model=list[schemas.Record])
def read_all_record(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: User = Depends(current_user)):
    record = crud.get_all_records(db, skip=skip, limit=limit, user_id=user.id)
    return record


@record_router.get("/record/{record_id}", response_model=schemas.Record)
def read_one_record(record_id: int, db: Session = Depends(get_db), user: User = Depends(current_user)):
    db_record = crud.get_record(db, record_id=record_id, user_id=user.id)
    if db_record is None:
        raise HTTPException(status_code=404, detail="Запись не найдена.")
    return db_record


@record_router.patch("/record", response_model=schemas.Record)
def update_record(record: schemas.RecordUpdate, db: Session = Depends(get_db)):
    db_record = crud.update_record(db, record=record)
    if db_record is None:
        raise HTTPException(status_code=404, detail="Запись не найдена.")
    return db_record


@record_router.delete("/record", response_model=schemas.Record)
def delete_record(record_id: int, db: Session = Depends(get_db)):
    db_record = crud.delete_record(db, record_id=record_id)
    # if db_record is not None:
    #     raise HTTPException(status_code=400, detail="Запись не удалена.")
    return db_record
