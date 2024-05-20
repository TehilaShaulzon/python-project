
from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException

from models.income import Income
from services.incomeService import get_income_by_user_id, add_new_income, update_new_income
from validations.income_validations import check_user_id, check_id_exist

Income_Router = APIRouter()

@Income_Router.get("/{userId}")
async def get_income(userId:int=Depends(check_id_exist)):
  try:
    income=await get_income_by_user_id(userId)
  except Exception as e:
    raise e
  return income

@Income_Router.post("/add_income/{user_id}")
async def add_income(new_income: Income, user_id=Depends(check_user_id)):
    try:
        await add_new_income(new_income)
    except Exception as e:
        raise e
    return "success"

@Income_Router.put("/{user_id}/{income_id}", response_model=Income)
async def update_income(new_income: Income,income_id, user_id=Depends(check_user_id)):
    try:
        result = await update_new_income(new_income,income_id,user_id)
    except Exception as e:
        raise e
    return result
