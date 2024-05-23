from datetime import datetime
from pydantic import BaseModel, field_validator


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

    def __init__(self, id: int, user_id: int, description: str, amount: float, date: datetime):
        super().__init__(id=id, user_id=user_id, description=description, amount=amount, date=date)


    @field_validator('amount')
    def validate_amount(cls,value):
            print("in try")
            if value > 0:
                return value
            else:
                raise ValueError("the amount cant be negative or zero")

#
