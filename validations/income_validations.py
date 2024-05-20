"""
validations/income_validations.py

This module defines validation functions related to income operations.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.income.Income: Pydantic model for representing income data.
    - services.userService.collection: MongoDB collection for storing user data.
    - services.incomeService.collection: MongoDB collection for storing income data.

Functions:
    - check_user_id: Validate user ID for adding income.
    - check_id_exist: Check if user ID exists and has income.
    - check_user_id_for_delete: Validate user ID for deleting income.


"""

from fastapi import HTTPException
from models.income import Income
from services.userService import collection as user_collection
from services.incomeService import collection as income_collection


def check_user_id(new_income: Income, user_id: int):
    """
    Validate user ID for adding income.

    Args:
        new_income (Income): New income data.
        user_id (int): ID of the user.

    Returns:
        int: Validated user ID.

    Raises:
        HTTPException: If an error occurs during validation.
    """
    print("popop")
    print(new_income)
    try:
        result = list(user_collection.find({"id": new_income.user_id}))
        user_id = int(user_id)
    except Exception as e:
        print("except")
        print(e)
        raise e
    if len(result) == 0:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if user_id != new_income.user_id:
        raise HTTPException(status_code=401, detail="The user ID you inserted is incorrect")

    return user_id


def check_id_exist(user_id: int):
    """
    Check if user ID exists and has income.

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
        result = list(income_collection.find({"user_id": user_id}))
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="You don't have any income")
    except Exception as e:
        raise e
    return user_id


def check_user_id_for_delete(income_id: int, user_id: int):
    """
    Validate user ID for deleting income.

    Args:
        income_id (int): ID of the income.
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
        result_income_id = list(income_collection.find({"id": income_id, "user_id": user_id}))
        if len(result_income_id) == 0:
            raise HTTPException(status_code=401, detail="Not have income with this ID")
    except Exception as e:
        raise e
    return user_id
