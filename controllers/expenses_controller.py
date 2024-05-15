import uvicorn

from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,constr, ValidationError, validator, field_validator

from models.expenses import Expenses
from services.expensesService import  add_new_expenses
from validations.expenses_validations import check_user_id

Expenses_Router = APIRouter()

@Expenses_Router.get("/{userId}")
async def get_expenses(userId:int):
  try:
   expenses=await get_expenses(userId)
  except :
    raise HTTPException(status_code=400, detail="oops... an error occurred" )
  return expenses

@Expenses_Router.post("/add_expenses/{user_id}")
async def add_expenses(new_expenses: Expenses, user_id=Depends(check_user_id)):
    try:
        print(user_id)
        print(new_expenses)
        await add_new_expenses(new_expenses)
    except :
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "success"
