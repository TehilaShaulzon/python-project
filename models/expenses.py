from datetime import datetime

from pydantic import BaseModel


class Expenses(BaseModel):
    id: int
    user_id: int
    description: str
    amount:float
    date: datetime
