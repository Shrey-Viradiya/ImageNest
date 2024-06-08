"""
This module defines the Board model.

The Board model represents a board in the application.
It includes attributes for the board's id, name, description, owner_id,
and is_private status.
"""

from pydantic import BaseModel


class Board(BaseModel):
    """
    Represents a board in the application.

    Attributes:
        id (int): The unique identifier of the board.
        name (str): The name of the board.
        description (str): A brief description of the board.
        owner_id (int): The identifier of the user who owns the board.
        is_private (bool): Whether the board is private or not.
    """

    id: int
    name: str
    description: str
    owner_id: int
    is_private: bool
