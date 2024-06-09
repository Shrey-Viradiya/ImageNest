"""
This module defines the Pin model.

The Pin model represents a pin in the application.
It includes attributes for the pin's
title, description, image_url, board_id, owner_id, and is_private status.
"""

from typing import Union

from pydantic import BaseModel


class Pin(BaseModel):
    """
    Represents a pin in the application.

    Attributes:
        title (str): The title of the pin.
        description (str): A brief description of the pin.
        image_url (str): The URL of the pin's image.
        board_id (int): The identifier of the board the pin belongs to.
        owner_id (int): The identifier of the user who owns the pin.
        is_private (bool): Whether the pin is private or not.
    """

    id: Union[int, None] = None
    title: str
    description: str
    image_url: str
    board_id: int
    owner_id: int
    is_private: bool
