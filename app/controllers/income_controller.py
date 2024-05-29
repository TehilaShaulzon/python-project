"""
income_controller.py

This module defines the API routes for managing income using FastAPI. It includes endpoints for retrieving, adding, updating, and deleting income records.

Modules Imported:
    - fastapi.FastAPI, Depends, APIRouter: FastAPI classes for creating the application instance, handling dependencies, and routing.
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.income.Income: Pydantic model for income.
    - services.incomeService: Service functions for performing CRUD operations on income.
    - validations.income_validations: Validation functions to check user and income IDs.

Routes:
    - GET /{userId}: Retrieve income records for a specific user.
    - POST /add_income/{user_id}: Add new income records for a user.
    - PUT /{user_id}/{income_id}: Update existing income records for a user.
    - DELETE /delete_income/{income_id}/{user_id}: Delete an income record for a user.


"""

from fastapi import FastAPI, Depends, APIRouter
from fastapi import HTTPException

from app.models.income import Income
from app.services.income_service import get_income_by_user_id, add_new_income, update_new_income, delete_one_income
from validations.income_validations import check_user_id, check_id_exist, check_user_id_for_delete

Income_Router = APIRouter()


@Income_Router.get("/{userId}")
async def get_income(userId: int = Depends(check_id_exist)):
    """
    Retrieve income records for a specific user.

    Args:
        userId (int): The ID of the user whose income records are to be retrieved.

    Returns:
        List[Income]: A list of income records for the specified user.

    Raises:
        HTTPException: If an error occurs during retrieval.
    """
    try:
        income = await get_income_by_user_id(userId)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return income


@Income_Router.post("/add_income/{user_id}")
async def add_income(new_income: Income, user_id=Depends(check_user_id)):
    """
    Add new income records for a user.

    Args:
        new_income (Income): The new income records to be added.
        user_id (int): The ID of the user to whom the income records belong.

    Returns:
        str: Success message.

    Raises:
        HTTPException: If an error occurs during addition.
    """
    try:
        await add_new_income(new_income)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return "success"


@Income_Router.put("/{user_id}/{income_id}", response_model=Income)
async def update_income(new_income: Income, income_id, user_id=Depends(check_user_id)):
    """
    Update existing income records for a user.

    Args:
        new_income (Income): The updated income data.
        income_id (str): The ID of the income record to be updated.
        user_id (int): The ID of the user to whom the income records belong.

    Returns:
        Income: The updated income record.

    Raises:
        HTTPException: If an error occurs during update.
    """
    try:
        result = await update_new_income(new_income, income_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return result


@Income_Router.delete("/delete_income/{income_id}/{user_id}")
async def delete_income(income_id, user_id=Depends(check_user_id_for_delete)):
    """
    Delete an income record for a user.

    Args:
        income_id (str): The ID of the income record to be deleted.
        user_id (int): The ID of the user to whom the income record belongs.

    Returns:
        str: Success message.

    Raises:
        HTTPException: If an error occurs during deletion.
    """
    try:
        await delete_one_income(income_id, user_id)
    except:
        raise HTTPException(status_code=401, detail="Oops... an error occurred")
    return "success"
