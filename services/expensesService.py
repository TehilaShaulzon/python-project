"""
services/expensesService.py

This module defines service functions related to expenses management.

Modules Imported:
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - dataAccess.dataAccess: Module for accessing the database.
    - models.expenses.Expenses: Pydantic model for representing expenses data.
    - models.users.User: Pydantic model for representing user data.

Global Variables:
    - collection: MongoDB collection for storing expenses data.
    - expenses_id: Counter for generating unique expenses IDs.

Functions:
    - get_expenses_by_user_id: Retrieve expenses data by user ID.
    - add_new_expenses: Add new expenses data.
    - update_new_expenses: Update existing expenses data.
    - delete_one_expenses: Delete a specific expenses record.


"""

from fastapi import HTTPException
from dataAccess.dataAccess import db
from models.expenses import Expenses
from models.users import User

# Select collection
collection = db['expenses']
# Initialize expenses_id
expenses_id = (collection.find({}, {'id': 1}).sort('id', -1)[0])["id"]


async def get_expenses_by_user_id(user_id: int):
    """
    Retrieve expenses data by user ID.

    Args:
        user_id (int): ID of the user.

    Returns:
        list: List of expenses records for the specified user.

    Raises:
        HTTPException: If an error occurs during data retrieval.
    """
    print("service")
    try:
        expenses_by_user_id = list(collection.find({"user_id": user_id}))
        for i in expenses_by_user_id:
            i.pop("_id")
    except Exception as e:
        raise e

    return expenses_by_user_id


async def add_new_expenses(new_expenses: Expenses):
    """
    Add new expenses data.

    Args:
        new_expenses (Expenses): New expenses data to be added.

    Raises:
        HTTPException: If an error occurs during data insertion.
    """
    try:
        global expenses_id
        expenses_id += 1
        new_expenses.id = expenses_id
        collection.insert_one(new_expenses.dict())
    except Exception as e:
        raise e


async def update_new_expenses(new_expenses: Expenses, expenses_id: str, user_id: int):
    """
    Update existing expenses data.

    Args:
        new_expenses (Expenses): Updated expenses data.
        expenses_id (str): ID of the expenses record to update.
        user_id (int): ID of the user associated with the expenses record.

    Returns:
        Expenses: The updated expenses data.

    Raises:
        HTTPException: If an error occurs during data update.
    """
    try:
        if user_id != new_expenses.user_id:
            raise HTTPException(status_code=401, detail="The user ID you inserted is incorrect")
        if expenses_id != str(new_expenses.id):
            raise HTTPException(status_code=401, detail="The expenses ID you inserted is incorrect")
        result = list(collection.find({"id": new_expenses.id, "user_id": new_expenses.user_id}))
        if len(result) == 0:
            raise HTTPException(status_code=404, detail="This user does not have this expenses")
        else:
            collection.update_one({"id": int(expenses_id)}, {"$set": new_expenses.dict()})
    except Exception as e:
        raise e

    return new_expenses


async def delete_one_expenses(expenses_id: str, user_id: int):
    """
    Delete a specific expenses record.

    Args:
        expenses_id (str): ID of the expenses record to delete.
        user_id (int): ID of the user associated with the expenses record.

    Raises:
        HTTPException: If an error occurs during data deletion.
    """
    try:
        collection.delete_one({"id": int(expenses_id), "user_id": user_id})
    except Exception as e:
        raise e
