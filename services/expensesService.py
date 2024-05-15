from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.expenses import Expenses
from models.users import User

collection = db['expenses']


async def getExpenses(user_id):
    expenses = collection.find({"id": user_id}).collection()
    # try:
    #
    # except:
    #      raise ValueError("error!!!")

    return expenses
async def add_new_expenses(new_expenses:Expenses):
    try:
        collection.insert_one(new_expenses.dict())
    except Exception as e:
        raise e
