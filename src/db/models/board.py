# pylint: disable=R0903

"""
This module defines the Board model.

The Board model represents a board in the application.
It includes attributes for the board's id, name, description, owner_id,
and is_private status.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Board(Base):
    """
    Represents a board in the application.

    Attributes:
        id (int): The unique identifier of the board.
        name (str): The name of the board.
        description (str): A brief description of the board.
        is_private (int): Whether the board is private or not.
        owner_id (int): The identifier of the user who owns the board.
    """

    __tablename__ = "boards"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    is_private = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="boards")
    pins = relationship("Pin", back_populates="board")
