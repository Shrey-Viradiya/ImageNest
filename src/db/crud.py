"""
This Module defines the CRUD operations for the application.
"""

from sqlalchemy.orm import Session

from src.db.models.user import User as UserModel
from src.models.user_create import UserCreate


def get_user_by_email(db: Session, email: str):
    """
    Get a user by email address.
    :param db: The database session.
    :param email: The email address of the user.
    :return: The user with the given email address.
    """
    return db.query(UserModel).filter(UserModel.email == email).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.
    :param db: The database session
    :param user: The user to create.
    :return: The created user.
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserModel(
        name=user.name,
        email=user.email,
        gender=user.gender,
        password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    """
    Get a user by ID.
    :param db: The database session.
    :param user_id: The ID of the user.
    :return: The user with the given ID.
    """
    return db.query(UserModel).filter(UserModel.id == user_id).first()
