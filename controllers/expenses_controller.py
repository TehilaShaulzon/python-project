"""
expenses_controller.py

This module defines the API routes for managing expenses using FastAPI. It includes endpoints for retrieving, adding, updating, and deleting expenses.

Modules Imported:
    - fastapi.FastAPI, Depends, APIRouter: FastAPI classes for creating the application instance, handling dependencies, and routing.
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - models.expenses.Expenses: Pydantic model for expenses.
    - services.expensesService: Service functions for performing CRUD operations on expenses.
    - validations.expenses_validations: Validation functions to check user and expense IDs.

Routes:
    - GET /{userId}: Retrieve expenses for a specific user.
    - POST /add_expenses/{user_id}: Add new expenses for a user.
    - PUT /{user_id}/{expenses_id}: Update existing expenses for a user.
    - DELETE /delete_expenses/{expenses_id}/{user_id}: Delete an expense for a user.


"""

from fastapi import FastAPI, Depends, APIRouter
from fastapi import HTTPException

from models.expenses import Expenses
from services.expensesService import add_new_expenses, get_expenses_by_user_id, update_new_expenses, delete_one_expenses
from validations.expenses_validations import check_user_id, check_id_exist, check_user_id_for_delete

Expenses_Router = APIRouter()


@Expenses_Router.get("/{userId}")
async def get_expenses(userId: int = Depends(check_id_exist)):
    """
    Retrieve expenses for a specific user.

    Args:
        userId (int): The ID of the user whose expenses are to be retrieved.

    Returns:
        List[Expenses]: A list of expenses for the specified user.

    Raises:
        HTTPException: If an error occurs during retrieval.
    """
    try:
        expenses = await get_expenses_by_user_id(userId)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return expenses


@Expenses_Router.post("/add_expenses/{user_id}")
async def add_expenses(new_expenses: Expenses, user_id=Depends(check_user_id)):
    """
    Add new expenses for a user.

    Args:
        new_expenses (Expenses): The new expenses to be added.
        user_id (int): The ID of the user to whom the expenses belong.

    Returns:
        str: Success message.

    Raises:
        HTTPException: If an error occurs during addition.
    """
    try:
        await add_new_expenses(new_expenses)
    except:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return "success"


@Expenses_Router.put("/{user_id}/{expenses_id}", response_model=Expenses)
async def update_expenses(new_expenses: Expenses, expenses_id, user_id=Depends(check_user_id)):
    """
    Update existing expenses for a user.

    Args:
        new_expenses (Expenses): The updated expenses data.
        expenses_id (str): The ID of the expense to be updated.
        user_id (int): The ID of the user to whom the expenses belong.

    Returns:
        Expenses: The updated expenses.

    Raises:
        HTTPException: If an error occurs during update.
    """
    try:
        result = await update_new_expenses(new_expenses, expenses_id, user_id)
    except Exception as e:
        raise e
    return result


@Expenses_Router.delete("/delete_expenses/{expenses_id}/{user_id}")
async def delete_expenses(expenses_id, user_id=Depends(check_user_id_for_delete)):
    """
    Delete an expense for a user.

    Args:
        expenses_id (str): The ID of the expense to be deleted.
        user_id (int): The ID of the user to whom the expense belongs.

    Returns:
        str: Success message.

    Raises:
        HTTPException: If an error occurs during deletion.
    """
    try:
        await delete_one_expenses(expenses_id, user_id)
    except:
        raise HTTPException(status_code=401, detail="Oops... an error occurred")
    return "success"
