from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.orm import sessionmaker, DeclarativeMeta, declarative_base

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# postgresql://%(DB_USER)s:%(DB_PASS)s@%(DB_HOST)s:%(DB_PORT)s/%(DB_NAME)s
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

Base: DeclarativeMeta = declarative_base()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Ассинхронное подключение

# engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
#
#
# async def init_db():
#     async with engine.begin() as conn:
#         # await conn.run_sync(SQLModel.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#
#
# async def get_session() -> AsyncSession:
#     async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#     async with async_session() as session:
#         yield session
