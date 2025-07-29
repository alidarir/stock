from pydantic_settings import BaseSettings
from sqlalchemy.orm import Session


class DatabaseSettings(BaseSettings):
    database_url: str = "sqlite:///./test.db"

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()