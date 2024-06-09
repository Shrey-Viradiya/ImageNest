"""
Application Start Point Where FastAPI is Configured and Endpoints are Defined.
"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.db import crud
from src.db.session import SessionLocal
from src.models.board import Board
from src.models.pin import Pin
from src.models.user import User
from src.models.user_create import UserCreate

app = FastAPI()

users = []
boards = []
pins = []


def get_db():
    """
    Get the database session.
    :return: The database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    :param user: The user to create.
    :param db: The database session.
    :return: The created user.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.
    :param user_id: The ID of the user.
    :param db: The database session.
    :return: The user with the given ID.
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/boards/")
async def create_board(board: Board):
    """
    Create a new board and add it to the boards list.

    Args:
        board (board): The board to be created.

    Returns:
        board: The created board.
    """
    boards.append(board)
    return board


@app.get("/boards/")
async def read_boards():
    """
    Get the list of all boards.

    Returns:
        list: The list of boards.
    """
    return boards


@app.post("/pins/")
async def create_pin(pin: Pin):
    """
    Create a new pin and add it to the pins list.

    Args:
        pin (pin): The pin to be created.

    Returns:
        pin: The created pin.
    """
    pins.append(pin)
    return pin


@app.get("/pins/")
async def read_pins():
    """
    Get the list of all pins.

    Returns:
        list: The list of pins.
    """
    return pins
