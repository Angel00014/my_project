import json
import os
import sys
from datetime import datetime

from fastapi import Depends
from confluent_kafka import Consumer

from sqlalchemy.orm import Session

from fastapi_users import FastAPIUsers

import src.back_list.models
from ..auth.auth import auth_backend
from ..auth.manager import get_user_manager
from ..auth.models import User
from ..database import SessionLocal

TOPIC = os.environ.get("TOPIC")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


conf = {
    'bootstrap.servers': "kafka:9092",
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

c = Consumer(conf)
c.subscribe(["test_topic"])


def process_message(message, db: Session, user_id: User = Depends(current_user)):
    content = json.loads(message.value())

    print(f"Сообщение: 4", f"{content}", file=sys.stderr)

    record_from_kafka = src.back_list.models.Record(
        name=content['name'],
        url=content["url"],
        category_id=content["category_id"],
        created_at=datetime.now(),
        user_id=1
    )

    db.add(record_from_kafka)
    db.commit()
    db.refresh(record_from_kafka)
    db.close()


def consume_messages():
    db = get_db()
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                print(f"Сообщение: Новое сообщение не обнаружено", file=sys.stderr)
                continue
            if msg.error():
                print(f"Сообщение: {msg.error()}", file=sys.stderr)
                print(msg.error())
                break
            print(f"Сообщение: {msg}", file=sys.stderr)
            process_message(msg, db=db)

    except KeyboardInterrupt:
        pass

    finally:
        db.close()
        c.close()

# Вызов функции для чтения сообщений
consume_messages()
