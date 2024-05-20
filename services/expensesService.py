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


async def update_new_expenses(new_expenses: Expenses,expenses_id,user_id):
    try:

       if user_id!= new_expenses.user_id:
           raise HTTPException(status_code=401, detail="the user id you insert is incorrect")
       if expenses_id != str(new_expenses.id):
           raise HTTPException(status_code=401, detail="the expenses id you insert is incorrect")
       result=list(collection.find({"id": new_expenses.id,"user_id":new_expenses.user_id}))
       if len(result)==0:
        raise HTTPException(status_code=404, detail="this user dont have this expenses")
       else:
        collection.update_one({"id": int(expenses_id)}, {"$set": new_expenses.dict()})
    except Exception as e:
         raise e

    return new_expenses

