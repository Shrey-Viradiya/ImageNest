"""
This module defines the Gender enum.

The Gender enum represents the gender options for a user in the application.
It includes options for "Male" and "Female".
"""

from enum import Enum


class Gender(str, Enum):
    """
    Enum Options for Gender of the User
    """

    MALE = "Male"
    FEMALE = "Female"
