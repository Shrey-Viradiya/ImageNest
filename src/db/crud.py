"""
This Module defines the CRUD operations for the application.
"""

from sqlalchemy import func
from sqlalchemy.orm import Session

from src.db.models.board import Board as BoardModel
from src.db.models.pin import Pin as PinModel
from src.db.models.user import User as UserModel
from src.models.board import Board
from src.models.pin import Pin
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


def create_board(db: Session, board: Board):
    """
    Create a new board in the database.
    :param db: The database session.
    :param board: The board to create.
    :return: The created board.
    """
    db_board = BoardModel(
        name=board.name,
        description=board.description,
        owner_id=board.owner_id,
        is_private=1 if board.is_private else 0,
    )
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board


def get_board(db: Session, board_id: int):
    """
    Get a board by ID.
    :param db: The database session.
    :param board_id: The ID of the board.
    :return: The board with the given ID.
    """
    return db.query(BoardModel).filter(BoardModel.id == board_id).first()


def get_boards_by_owner(db: Session, user_id: int):
    """
    Get all boards owned by a user.
    :param db: The database session.
    :param user_id: The ID of the user.
    :return: A list of boards owned by the user.
    """
    return db.query(BoardModel).filter(BoardModel.owner_id == user_id).all()


def create_pin(db: Session, pin: Pin):
    """
    Create a new pin in the database.
    :param db: The database session.
    :param pin: The pin to create.
    :return: The created pin.
    """
    db_pin = PinModel(
        title=pin.title,
        description=pin.description,
        image_url=pin.image_url,
        board_id=pin.board_id,
        owner_id=pin.owner_id,
        thumbnail_url=pin.thumbnail_url,
        is_private=1 if pin.is_private else 0,
    )
    db.add(db_pin)
    db.commit()
    db.refresh(db_pin)
    return db_pin


def get_pin(db: Session, pin_id: int):
    """
    Get a pin by ID.
    :param db: The database session.
    :param pin_id: The ID of the pin.
    :return: The pin with the given ID.
    """
    return db.query(PinModel).filter(PinModel.id == pin_id).first()


def get_random_public_pins(db: Session, number: int):
    """
    Get random
    :param db: The database session.
    :param number: number of pin.
    :return: The pin with the given ID.
    """
    # pylint: disable=E1102
    return (
        db.query(PinModel)
        .filter(PinModel.is_private == 0)
        .order_by(func.random())
        .limit(number)
        .all()
    )


def get_pins_by_board(db: Session, board_id: int):
    """
    Get all pins for a board.
    :param db: The database session.
    :param board_id: The ID of the board.
    :return: A list of pins for the board.
    """
    return db.query(PinModel).filter(PinModel.board_id == board_id).all()
