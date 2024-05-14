from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    id: int
    description: str
    userId: int
    expensesDate: datetime
