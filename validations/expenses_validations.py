"""
validations/expenses_validations.py

This module defines validation functions related to expenses operations.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.expenses.Expenses: Pydantic model for representing expenses data.
    - services.userService.collection: MongoDB collection for storing user data.
    - services.expensesService.collection: MongoDB collection for storing expenses data.

Functions:
    - check_user_id: Validate user ID for adding expenses.
    - check_id_exist: Check if user ID exists and has expenses.
    - check_user_id_for_delete: Validate user ID for deleting expenses.


"""

from fastapi import HTTPException
from models.expenses import Expenses
from services.userService import collection as user_collection
from services.expensesService import collection as expenses_collection


def check_user_id(new_expenses: Expenses, user_id: int):
    """
    Validate user ID for adding expenses.

    Args:
        new_expenses (Expenses): New expenses data.
        user_id (int): ID of the user.

    Returns:
        int: Validated user ID.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    print("popop")
    print(new_expenses)
    try:
        result = list(user_collection.find({"id": new_expenses.user_id}))
        print("lll")
        print(result[0])
        user_id = int(user_id)
    except Exception as e:
        print("except")
        print(e)
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    if len(result) == 0 or user_id != new_expenses.user_id:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user_id


def check_id_exist(user_id: int):
    """
    Check if user ID exists and has expenses.

    Args:
        user_id (int): ID of the user.

    Returns:
        int: Validated user ID.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    try:
        user_id = int(user_id)
        result = list(user_collection.find({"id": user_id}))
        if len(result) == 0:
            raise HTTPException(status_code=401, detail="Unauthorized")
        result = list(expenses_collection.find({"user_id": user_id}))
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="You don't have any expenses")
    except Exception as e:
        raise e
    return user_id


def check_user_id_for_delete(expenses_id: int, user_id: int):
    """
    Validate user ID for deleting expenses.

    Args:
        expenses_id (int): ID of the expenses.
        user_id (int): ID of the user.

    Returns:
        int: Validated user ID.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    try:
        user_id = int(user_id)
        result_user_id = list(user_collection.find({"id": user_id}))
        print(len(result_user_id))
        if len(result_user_id) == 0:
            raise HTTPException(status_code=401, detail="Unauthorized")
        result_expenses_id = list(expenses_collection.find({"id": expenses_id, "user_id": user_id}))
        if len(result_expenses_id) == 0:
            raise HTTPException(status_code=401, detail="Not have expenses with this ID")
    except Exception as e:
        raise e
    return user_id















