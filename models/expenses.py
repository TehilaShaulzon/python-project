from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    id: int
    description: str
    user_id: int
    expensesDate: datetime
