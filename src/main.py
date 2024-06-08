"""
Application Start Point Where FastAPI is Configured and Endpoints are Defined.
"""

from fastapi import FastAPI

from src.models.board import Board
from src.models.pin import Pin
from src.models.user import User

app = FastAPI()

users = []
boards = []
pins = []


@app.post("/users/")
async def create_user(user: User):
    """
    Create a new user and add it to the users list.

    Args:
        user (user): The user to be created.

    Returns:
        user: The created user.
    """
    users.append(user)
    return user


@app.get("/users/")
async def read_users():
    """
    Get the list of all users.

    Returns:
        list: The list of users.
    """
    return users


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
