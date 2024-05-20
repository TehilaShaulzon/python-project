from datetime import datetime

from pydantic import BaseModel


class Income(BaseModel):
    id: int
    user_id: int
    description: str
    amount: float
    expensesDate: datetime