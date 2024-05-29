"""
services/user_service.py

This module defines service functions related to user management.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - data_access.data_access: Module for accessing the database.
    - models.users.User: Pydantic model for representing user data.

Global Variables:
    - collection: MongoDB collection for storing user data.
    - user_id: Counter for generating unique user IDs.

Functions:
    - login: Authenticate user login.
    - signUp: Register a new user.
    - update: Update user details.


"""

from fastapi import HTTPException
from data_access.data_access import db
from decorators.logger_decorator import logger
from models.users import User

# Select collection
collection = db['users']
# Initialize user_id
user_id = (collection.find({}, {'id': 1}).sort('id', -1)[0])["id"]

@logger("log.txt")

async def login(name: str, password: str):
    """
    Authenticate user login.

    Args:
        name (str): User name.
        password (str): User password.

    Returns:
        str: Greeting message for successful login.

    Raises:
        HTTPException: If login fails.
    """
    try:
        print(name + " " + password)
        result = list(collection.find({"name": name, "password": password}))
        if len(result) == 0:
            raise HTTPException(status_code=401, detail="You are not registered")
        else:
            return f"Hello {name} Your ID: {result[0]['id']}"
    except Exception as e:
        raise e

@logger("log.txt")

async def signUp(user: User):
    """
    Register a new user.

    Args:
        user (User): User data to be registered.

    Returns:
        str: Greeting message for successful registration.

    Raises:
        HTTPException: If user registration fails.
    """
    try:
        global user_id
        user_id += 1
        user.id = user_id
        collection.insert_one(user.dict())
    except Exception as e:
        raise HTTPException(status_code=401, detail="An error occurred")
    return f"Hello {user.name}"


async def update(new_user: User, user_id: int):
    """
    Update user details.

    Args:
        new_user (User): Updated user data.
        user_id (int): ID of the user to update.

    Returns:
        User: The updated user data.

    Raises:
        HTTPException: If user update fails.
    """
    try:
        if user_id != new_user.id:
            raise HTTPException(status_code=401, detail="The ID you inserted is incorrect")
        result = list(collection.find({"id": new_user.id}))
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="This ID is not found")
        else:
            collection.update_one({"id": int(user_id)}, {"$set": new_user.dict()})
    except Exception as e:
        raise e

    return new_user









