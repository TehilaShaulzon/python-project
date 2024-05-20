"""
models/users.py

This module defines the Pydantic model for representing user data.

Modules Imported:
    - pydantic.BaseModel, constr, ValidationError, validator, field_validator: Pydantic classes for defining data models and validation.

Class:
    - User: Pydantic model representing user data with fields for ID, name, password, and email.


"""

from pydantic import BaseModel, constr

class User(BaseModel):
    """
    Pydantic model representing user data.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        password (str): The password of the user.
        email (str): The email address of the user.
    """
    id: int
    name: str
    password: str
    email: str
