# pylint: disable=R0913

"""
Application Start Point Where FastAPI is Configured and Endpoints are Defined.
"""
import os
import uuid

import aiofiles
from fastapi import Depends, FastAPI, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.constants import S3_BUCKET
from src.db import crud
from src.db.object_store import upload_to_s3
from src.db.session import SessionLocal
from src.models.board import Board
from src.models.pin import Pin
from src.models.user import User
from src.models.user_create import UserCreate

app = FastAPI()


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
async def create_board(board: Board, db: Session = Depends(get_db)):
    """
    Create a new board and add it to the boards list.
    :param board: The board to create.
    :param db: The database session.
    :return: The created board.
    """
    db_user = crud.get_user(db, user_id=board.owner_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_board(db=db, board=board)


@app.get("/boards/{board_id}")
async def read_boards(board_id: int, db: Session = Depends(get_db)):
    """
    Get a board by ID.
    :param board_id: The ID of the board.
    :param db: The database session.
    :return: The board with the given ID.
    """
    db_board = crud.get_board(db, board_id=board_id)
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board


@app.get("/boards/user/{user_id}")
async def read_boards_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a board by ID.
    :param board_id: The ID of the board.
    :param db: The database session.
    :return: The board with the given ID.
    """
    return crud.get_boards_by_owner(db, user_id=user_id)


@app.post("/pins/")
async def create_pin(
    title: str = Form(...),
    description: str = Form(...),
    board_id: int = Form(...),
    owner_id: int = Form(...),
    is_private: bool = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Create a new pin and add it to the pins list.
    :param title: The title of the pin.
    :param description: A brief description of the pin.
    :param board_id: The ID of the board the pin belongs to.
    :param owner_id: The ID of the user who owns the pin.
    :param is_private: Whether the pin is private or not.
    :param file: The image file to upload.
    :param db: The database session.
    :return: The created pin.
    """
    db_user = crud.get_user(db, user_id=owner_id)
    db_board = crud.get_board(db, board_id=board_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")

    filename, temp_file_path = await get_file_name(file)

    image_url = upload_to_s3(temp_file_path, S3_BUCKET, filename)

    os.remove(temp_file_path)

    pin = Pin(
        title=title,
        description=description,
        board_id=board_id,
        owner_id=owner_id,
        is_private=is_private,
        image_url=image_url,
    )
    return crud.create_pin(db=db, pin=pin)


async def get_file_name(file):
    """
    Get the file name.
    :param file: The file to get the name of.
    :return: The name of the file.
    """
    # Generate a random filename
    filename = str(uuid.uuid4())
    file_extension = file.filename.split(".")[-1]  # Get the file extension
    filename = (
        f"{filename}.{file_extension}"  # Append the file extension to the filename
    )
    # Save the file to a temporary location
    temp_file_path = f"/tmp/{filename}"
    async with aiofiles.open(temp_file_path, "wb") as buffer:
        data = await file.read()  # async read
        await buffer.write(data)
    return filename, temp_file_path


@app.get("/pins/{pin_id}")
async def get_pin(pin_id: int, db: Session = Depends(get_db)):
    """
    Get a pin by ID.
    :param pin_id: The ID of the pin.
    :param db: The database session.
    :return: The pin with the given ID.
    """
    return crud.get_pin(db, pin_id=pin_id)


@app.get("/pins/board/{board_id}")
async def get_pins_by_board(board_id: int, db: Session = Depends(get_db)):
    """
    Get all pins for a board.
    :param board_id: The ID of the board.
    :param db: The database session.
    :return: A list of pins for the board.
    """
    return crud.get_pins_by_board(db, board_id=board_id)
