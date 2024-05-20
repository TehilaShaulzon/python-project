"""
models/income.py

This module defines the Pydantic model for representing income data.

Modules Imported:
    - pydantic.BaseModel: Pydantic class for defining data models.
    - datetime.datetime: Class representing dates and times.

Class:
    - Income: Pydantic model representing income data with fields for ID, user ID, description, amount, and date.


"""

from datetime import datetime
from pydantic import BaseModel

class Income(BaseModel):
    """
    Pydantic model representing income data.

    Attributes:
        id (int): The unique identifier for the income record.
        user_id (int): The ID of the user to whom the income belongs.
        description (str): Description of the income.
        amount (float): Amount of the income.
        date (datetime): Date of the income.
    """
    id: int
    user_id: int
    description: str
    amount: float
    date: datetime
