"""
user_controller.py

This module defines the API routes for user authentication and management using FastAPI. It includes endpoints for user login, registration, and updating user details.

Modules Imported:
    - uvicorn: ASGI server for running FastAPI application.
    - fastapi.FastAPI, Depends, APIRouter: FastAPI classes for creating the application instance, handling dependencies, and routing.
    - fastapi.HTTPException: Exception class for handling HTTP errors.
    - pydantic.BaseModel, constr, ValidationError, validator, field_validator: Pydantic classes for defining data models and validation.
    - models.users.User: Pydantic model for user data.
    - services.userService: Service functions for user authentication and management.
    - validations.user_validations: Validation functions for user data.

Routes:
    - POST /login/: Authenticate user login.
    - POST /signUp/: Register a new user.
    - PUT /{id}: Update user details.

"""

import uvicorn
from fastapi import FastAPI, Depends, APIRouter
from fastapi import HTTPException
from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from app.models.users import User
from app.services.user_service import login, signUp, update
from validations.user_validations import sign_up_check_user

User_Router = APIRouter()




@User_Router.post("/login/")
async def login_user(name: str, password: str):
    """
    Authenticate user login.

    Args:
        name (str): User name.
        password (str): User password.

    Returns:
        str: Greeting message for successful login.

    Raises:
        Exception: If login fails.
    """
    try:
        print(name + " " + password)
        await login(name, password)
    except Exception as e:
        raise e
    return f"Hello {name}"


@User_Router.post("/signUp/")
async def add_user(user: User = Depends(sign_up_check_user)):
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
        print(user)
        await signUp(user)
    except ValidationError:
        raise HTTPException(status_code=400, detail="Oops... an error occurred")
    return f"Hello {user.name}"


@User_Router.put("/{id}", response_model=User)
async def update_user(newUser: User, id: int):
    """
    Update user details.

    Args:
        newUser (User): Updated user data.
        id (int): ID of the user to update.

    Returns:
        User: The updated user data.

    Raises:
        Exception: If user update fails.
    """
    try:
        result = await update(newUser, id)
    except Exception as e:
        print(e)
        raise e
    return result
