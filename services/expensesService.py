from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.expenses import Expenses
from models.users import User

collection = db['expenses']
expenses_id = (collection.find({}, { 'id': 1}).sort('id', -1)[0])["id"]


async def get_expenses_by_user_id(user_id):
    print("service")
    try:
        expenses_by_user_id =list(collection.find({"user_id": user_id}))
        for i in expenses_by_user_id:
            i.pop("_id")
    except Exception as e:
        raise e

    return expenses_by_user_id
async def add_new_expenses(new_expenses:Expenses):
    try:
        global expenses_id
        expenses_id += 1
        new_expenses.id = expenses_id
        collection.insert_one(new_expenses.dict())
    except Exception as e:
        raise e
