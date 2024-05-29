"""
models/users_service_test.py

This module defines the Pydantic model for representing user data.

Modules Imported:
    - pydantic.BaseModel, constr, ValidationError, validator, field_validator: Pydantic classes for defining data models and validation.

Class:
    - User: Pydantic model representing user data with fields for ID, name, password, and email.


"""
import re

from pydantic import BaseModel, constr, field_validator


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

    def __init__(self, id: int, name: str, password: str, email: str):
        super().__init__(id=id, name=name, password=password, email=email)

    @field_validator("id")
    def validate_id(cls, value):
        if value <= 0:
            raise ValueError("ה-ID חייב להיות מספר שלם חיובי.")

        return value

    @field_validator('name')
    def validate_name(cls, value):
        print("name valida")
        if len(value) < 3 or len(value) > 15:
            raise ValueError("שם המשתמש חייב להיות בין 3 ל-15 תווים.")
        if not re.match("^[A-Za-z][A-Za-z0-9]*$", value):
            raise ValueError("שם המשתמש חייב להתחיל באות ולהכיל רק תווים אלפאנומריים.")
        return value

    @field_validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("הסיסמה חייבת להיות לפחות 8 תווים.")
        if not re.search("[A-Z]", value):
            raise ValueError("הסיסמה חייבת לכלול לפחות אות אחת גדולה.")
        if not re.search("[a-z]", value):
            raise ValueError("הסיסמה חייבת לכלול לפחות אות אחת קטנה.")
        if not re.search("[0-9]", value):
            raise ValueError("הסיסמה חייבת לכלול לפחות מספר אחד.")
        if not re.search("[@#$%^&+=!?]", value):
            raise ValueError("הסיסמה חייבת לכלול לפחות תו מיוחד אחד.")
        return value

    @field_validator('email')
    def validate_email(cls, value):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, value):
            raise ValueError("כתובת האימייל אינה תקינה.")
        return value
