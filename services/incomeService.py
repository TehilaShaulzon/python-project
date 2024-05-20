from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.income import Income
from models.users import User

collection = db['income']
income_id =(collection.find({}, {'id': 1}).sort('id', -1)[0])["id"]



async def get_income_by_user_id(user_id):
    print("service")
    try:
        income_by_user_id =list(collection.find({"user_id": user_id}))
        for i in income_by_user_id:
            i.pop("_id")
    except Exception as e:
        raise e

    return income_by_user_id
async def add_new_income(new_income:Income):
    try:
        global income_id
        income_id += 1
        new_income.id = income_id
        collection.insert_one(new_income.dict())
    except Exception as e:
        raise e


async def update_new_income(new_income: Income,income_id,user_id):
    try:

       if user_id!= new_income.user_id:
           raise HTTPException(status_code=401, detail="the user id you insert is incorrect")
       if income_id != str(new_income.id):
           raise HTTPException(status_code=401, detail="the expenses id you insert is incorrect")
       result=list(collection.find({"id": new_income.id,"user_id":new_income.user_id}))
       if len(result)==0:
        raise HTTPException(status_code=404, detail="this user dont have this income")
       else:
        collection.update_one({"id": int(income_id)}, {"$set": new_income.dict()})
    except Exception as e:
         raise e

    return new_income

async def delete_one_income(income_id,user_id):
    try:
        collection.delete_one({"id": int(income_id), "user_id": user_id})
    except Exception as e:
        raise e

