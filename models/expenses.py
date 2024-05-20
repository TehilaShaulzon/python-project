"""
models/expenses.py

This module defines the Pydantic model for representing expenses data.

Modules Imported:
    - pydantic.BaseModel: Pydantic class for defining data models.
    - datetime.datetime: Class representing dates and times.

Class:
    - Expenses: Pydantic model representing expenses data with fields for ID, user ID, description, amount, and date.


"""

from datetime import datetime
from pydantic import BaseModel

class Expenses(BaseModel):
    """
    Pydantic model representing expenses data.

    Attributes:
        id (int): The unique identifier for the expense record.
        user_id (int): The ID of the user to whom the expense belongs.
        description (str): Description of the expense.
        amount (float): Amount of the expense.
        date (datetime): Date of the expense.
    """
    id: int
    user_id: int
    description: str
    amount: float
    date: datetime
