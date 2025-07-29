# db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ali_backend.conf.db import DatabaseSettings

settings = DatabaseSettings()

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
