"""
validations/user_validations.py

This module defines validation functions related to user operations.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.users.User: Pydantic model for representing user data.
    - services.userService.collection: MongoDB collection for storing user data.

Functions:
    - sign_up_check_user: Check if user data is valid for sign up.


"""
# from typing import

from fastapi import HTTPException
from app.models.users import User
from app.services.user_service import collection


def sign_up_check_user(new_user: User):
    """
    Check if user data is valid for sign up.

    Args:
        new_user (User): New user data.

    Returns:
        User: Validated user data.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    print(new_user)
    result = list(collection.find({"name": new_user.name, "password": new_user.password}))
    if len(result) != 0:
        raise HTTPException(status_code=401, detail="Name or password is incorrect")
    else:
        return new_user


# def validate_name(name):
#     # בדיקת אורך השם
#     if len(name) < 4 or len(name) > 10:
#         return False
#
#     # בדיקת שאין מספרים או תווים מיוחדים
#     if not re.match("^[a-zA-Zא-ת]+$", name):
#         return False
#
#     return True