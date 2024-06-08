"""
This module defines the Gender enum.

The Gender enum represents the gender options for a user in the application.
It includes options for "Male" and "Female".
"""

from pydantic import BaseModel

from src.enums.gender import Gender


class User(BaseModel):
    """
    Represents a user in the application.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        gender (gender): The gender of the user.
    """

    id: int
    name: str
    email: str
    gender: Gender
