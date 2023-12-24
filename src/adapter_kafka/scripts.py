import json
import sys
import logging

from confluent_kafka import Producer
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from fastapi_users import FastAPIUsers
from dataclasses import asdict

from src.config import BOOTSTRAP_URL, TOPIC

import src
from src.auth.auth import auth_backend
from src.auth.manager import get_user_manager
from src.adapter_kafka.crud import create_record_kafka

from src.database import SessionLocal
from src.auth.models import User

from src.back_list import crud, schemas
from sqlalchemy.orm import Session

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


kafka_router = APIRouter(
    prefix="/back-list/kafka",
    tags=["Kafka"])


@kafka_router.post("/record", response_model=schemas.RecordCreate)
def create_record(record: schemas.RecordCreate, db: Session = Depends(get_db), user: User = Depends(current_user)):
    serialized_record_dict = record.dict()
    serialized_record_byte = json.dumps(serialized_record_dict).encode('utf-8')

    p = Producer({'bootstrap.servers': BOOTSTRAP_URL})
    p.produce(TOPIC, key='key', value=serialized_record_byte)
    p.flush()

    return record