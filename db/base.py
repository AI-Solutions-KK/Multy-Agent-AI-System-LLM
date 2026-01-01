# PATH: db/base.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db.config import DB_TYPE, SQLITE_DB_PATH

if DB_TYPE == "sqlite":
    DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"
else:
    raise ValueError("Only sqlite supported for now")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
