from fastapi import HTTPException

from models.income import Income
from services.userService import collection as user_collection
from services.incomeService import collection as income_collection


def check_user_id(new_income: Income,user_id):
    print("popop")
    print(new_income)
    try:
        result = list(user_collection.find({"id": new_income.user_id}))
        user_id = int(user_id)
    except Exception as e:
        print("except")
        print(e)
        raise e
    if len(result) == 0 :
        raise HTTPException(status_code=401, detail="unauthorized")
    if  user_id != new_income.user_id:
        raise HTTPException(status_code=401, detail="the user id you insert is incorrect")

    return user_id

def check_id_exist(user_id):
    try:
        user_id=int(user_id)
        result = list(user_collection.find({"id":user_id}))
        if len(result)==0:
            raise HTTPException(status_code=401, detail="unauthorized")
        result=list(income_collection.find({"user_id":user_id}))
        if len(result)==0:
            raise HTTPException(status_code=404, detail="you dont have any income")
    except Exception as e:
        raise e
    return user_id

