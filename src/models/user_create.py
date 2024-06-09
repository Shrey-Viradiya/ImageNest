"""
Pydantic model for creating a user
"""

from src.models.user import User


class UserCreate(User):
    """
    Represents a user create request in the application.

    Attributes:
        All attributes from the User model are required.
        Password (str): The password of the user.
    """

    password: str
