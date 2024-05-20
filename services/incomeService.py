"""
services/incomeService.py

This module defines service functions related to income management.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - dataAccess.dataAccess: Module for accessing the database.
    - models.income.Income: Pydantic model for representing income data.
    - models.users.User: Pydantic model for representing user data.

Global Variables:
    - collection: MongoDB collection for storing income data.
    - income_id: Counter for generating unique income IDs.

Functions:
    - get_income_by_user_id: Retrieve income data by user ID.
    - add_new_income: Add new income data.
    - update_new_income: Update existing income data.
    - delete_one_income: Delete a specific income record.


"""

from fastapi import HTTPException
from dataAccess.dataAccess import db
from models.income import Income
from models.users import User

# Select collection
collection = db['income']
# Initialize income_id
income_id = (collection.find({}, {'id': 1}).sort('id', -1)[0])["id"]


async def get_income_by_user_id(user_id: int):
    """
    Retrieve income data by user ID.

    Args:
        user_id (int): ID of the user.

    Returns:
        list: List of income records for the specified user.

    Raises:
        HTTPException: If an error occurs during data retrieval.
    """
    print("service")
    try:
        income_by_user_id = list(collection.find({"user_id": user_id}))
        for i in income_by_user_id:
            i.pop("_id")
    except Exception as e:
        raise e

    return income_by_user_id


async def add_new_income(new_income: Income):
    """
    Add new income data.

    Args:
        new_income (Income): New income data to be added.

    Raises:
        HTTPException: If an error occurs during data insertion.
    """
    try:
        global income_id
        income_id += 1
        new_income.id = income_id
        collection.insert_one(new_income.dict())
    except Exception as e:
        raise e


async def update_new_income(new_income: Income, income_id: str, user_id: int):
    """
    Update existing income data.

    Args:
        new_income (Income): Updated income data.
        income_id (str): ID of the income record to update.
        user_id (int): ID of the user associated with the income record.

    Returns:
        Income: The updated income data.

    Raises:
        HTTPException: If an error occurs during data update.
    """
    try:
        if user_id != new_income.user_id:
            raise HTTPException(status_code=401, detail="The user ID you inserted is incorrect")
        if income_id != str(new_income.id):
            raise HTTPException(status_code=401, detail="The income ID you inserted is incorrect")
        result = list(collection.find({"id": new_income.id, "user_id": new_income.user_id}))
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="This user does not have this income")
        else:
            collection.update_one({"id": int(income_id)}, {"$set": new_income.dict()})
    except Exception as e:
        raise e

    return new_income


async def delete_one_income(income_id: str, user_id: int):
    """
    Delete a specific income record.

    Args:
        income_id (str): ID of the income record to delete.
        user_id (int): ID of the user associated with the income record.

    Raises:
        HTTPException: If an error occurs during data deletion.
    """
    try:
        collection.delete_one({"id": int(income_id), "user_id": user_id})
    except Exception as e:
        raise e
