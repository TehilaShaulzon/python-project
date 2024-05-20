from fastapi import HTTPException

from models.expenses import Expenses
from services.userService import collection as user_collection
from services.expensesService import collection as expenses_collection


def check_user_id(new_expenses: Expenses,user_id):
    print("popop")
    print(new_expenses)
    try:
        result = list(user_collection.find({"id": new_expenses.user_id}))
        print("lll")
        print(result[0])
        user_id = int(user_id)
    except Exception as e:
        print("except")
        print(e)
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    if len(result) == 0 or user_id != new_expenses.user_id:
        raise HTTPException(status_code=401, detail="unauthorized")

    return user_id

def check_id_exist(user_id):
    try:
        user_id=int(user_id)
        result = list(user_collection.find({"id":user_id}))
        if len(result)==0:
            raise HTTPException(status_code=401, detail="unauthorized")
        result=list(expenses_collection.find({"user_id":user_id}))
        if len(result)==0:
            raise HTTPException(status_code=404, detail="you dont have any expenses")
    except Exception as e:
        raise e
    return user_id

