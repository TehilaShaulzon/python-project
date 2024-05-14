from datetime import datetime


class Income(BaseModel):
    id: int
    description: str
    userId: int
    incomeDate: datetime
