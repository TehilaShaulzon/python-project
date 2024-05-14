from datetime import datetime

from pydantic import BaseModel


class Income(BaseModel):
    id: int
    description: str
    userId: int
    incomeDate: datetime
