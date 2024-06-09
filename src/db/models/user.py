# pylint: disable=R0903

"""
This module contains the User model for DB operations.
"""

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from src.enums.gender import Gender

from .base import Base


class User(Base):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        email (str): The email address of the user
        gender (gender): The gender of the user.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    gender = Column(Enum(Gender))
    password = Column(String)

    pins = relationship("Pin", back_populates="user")
    boards = relationship("Board", back_populates="user")
