from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, DeclarativeMeta, declarative_base

from src.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base: DeclarativeMeta = declarative_base()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
