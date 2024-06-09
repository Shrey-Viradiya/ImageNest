# pylint: disable=W0611

"""
Session Maker for the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.constants import DATABASE_URL
from src.db.models.base import Base
from src.db.models.board import Board  # Ensure Board model is imported
from src.db.models.pin import Pin  # Ensure Pin model is imported
from src.db.models.user import User  # Ensure User model is imported

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
