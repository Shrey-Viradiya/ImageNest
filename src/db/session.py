"""
Session Maker for the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.constants import DATABASE_URL
from src.db.models.base import Base

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
