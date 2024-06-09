# pylint: disable=R0903

"""
This module contains the Pin model.

The Pin model represents a pin in the application.
It includes attributes for the pin's id, title, and image_url.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Pin(Base):
    """
    Represents a pin in the application.

    Attributes:
        id (int): The unique identifier of the pin.
        title (str): The title of the pin.
        description (str): A brief description of the pin.
        image_url (str): The URL of the pin's image.
        board_id (int): The identifier of the board the pin belongs to.
        owner_id (int): The identifier of the user who owns the pin.
    """

    __tablename__ = "pins"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    image_url = Column(String)
    board_id = Column(Integer, ForeignKey("boards.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_private = Column(Integer)

    user = relationship("User", back_populates="pins")
    board = relationship("Board", back_populates="pins")
