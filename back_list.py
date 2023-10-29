from typing import List

from fastapi import FastAPI, Depends, HTTPException

# from models.Record import Records
from database import engine, SessionLocal
from models import models, pd_schemas
from scripts import crud
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My BackList"
)




# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.post("/category", response_model=pd_schemas.Category)
def create_category(category: pd_schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, category_name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Категория существует! Переименуйте свою категорию.")
    return crud.create_category(db=db, category=category)


@app.get("/category", response_model=list[pd_schemas.Category])
def read_all_category(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    category = crud.get_all_category(db, skip=skip, limit=limit)
    return category


@app.get("/category/{category_id}", response_model=pd_schemas.Category)
def read_one_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена.")
    return db_category


@app.post("/record", response_model=pd_schemas.Record)
def create_record(record: pd_schemas.RecordCreate, db: Session = Depends(get_db)):
    db_record = crud.get_record_by_name(db, record_name=record.name)
    if db_record:
        raise HTTPException(status_code=400, detail="Наименование уже существует! Выберете другое наименование")
    return crud.create_record(db=db, record=record)


@app.get("/record", response_model=list[pd_schemas.Record])
def read_all_record(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    record = crud.get_all_records(db, skip=skip, limit=limit)
    return record


@app.get("/record/{record_id}", response_model=pd_schemas.Record)
def read_one_record(record_id: int, db: Session = Depends(get_db)):
    db_record = crud.get_record(db, record_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=404, detail="Запись не найдена.")
    return db_record
