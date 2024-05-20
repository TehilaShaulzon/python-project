
from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException

from models.expenses import Expenses
from services.expensesService import add_new_expenses, get_expenses_by_user_id, update_new_expenses, delete_one_expenses
from validations.expenses_validations import check_user_id, check_id_exist, check_user_id_for_delete

Expenses_Router = APIRouter()

@Expenses_Router.get("/{userId}")
async def get_expenses(userId:int=Depends(check_id_exist)):
  try:
    expenses=await get_expenses_by_user_id(userId)
  except Exception as e:
    raise HTTPException(status_code=400, detail="oops... an error occurred" )
  return expenses

@Expenses_Router.post("/add_expenses/{user_id}")
async def add_expenses(new_expenses: Expenses, user_id=Depends(check_user_id)):
    try:
        await add_new_expenses(new_expenses)
    except :
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "success"

@Expenses_Router.put("/{user_id}/{expenses_id}", response_model=Expenses)
async def update_expenses(new_expenses: Expenses,expenses_id, user_id=Depends(check_user_id)):
    try:
        result = await update_new_expenses(new_expenses,expenses_id,user_id)
    except Exception as e:
        raise e
    return result


@Expenses_Router.delete("/delete_expenses/{expenses_id}/{user_id}")
async def delete_expenses(expenses_id, user_id=Depends(check_user_id_for_delete)):
    try:
        print(user_id)
        print(expenses_id)
        await delete_one_expenses(expenses_id,user_id)
    except :
        raise HTTPException(status_code=401, detail="oops... an error occurred")
    return "success"
