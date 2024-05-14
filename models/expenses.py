from datetime import datetime


class Expenses(BaseModel):
    id: int
    description: str
    userId: int
    expensesDate: datetime
