from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.expenses import Expenses
from models.users import User

collection = db['expenses']
expenses_id = (collection.find({}, { 'id': 1}).sort('id', -1)[0])["id"]


async def getExpenses(user_id):
    expenses = collection.find({"id": user_id}).collection()
    # try:
    #
    # except:
    #      raise ValueError("error!!!")

    return expenses
async def add_new_expenses(new_expenses:Expenses):
    try:
        global expenses_id
        expenses_id += 1
        new_expenses.id = expenses_id
        collection.insert_one(new_expenses.dict())
    except Exception as e:
        raise e
