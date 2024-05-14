import uvicorn

from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,constr, ValidationError, validator, field_validator

from models.users import User
from services.userService import login, signUp, update
from validations.user_validations import check_user

Expenses_Router = APIRouter()

#
#
#
#
# @User_Router.post("/login/")
# async def login_user(user: User):
#     try:
#        login(user)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=e)
#     return f"Hello {user.name}"
#
# @User_Router.post("/signUp/")
# async def add_user(user: User=Depends(check_user)):
#     try:
#         print(user)
#         await signUp(user)
#     except ValidationError:
#         raise HTTPException(status_code=400, detail="oops... an error occurred")
#     return f"Hello {user.name}"
#
# @User_Router.put("/{id}", response_model=User)
# async def update_user(newUser: User,id:int):
#
#     try:
#        msg=await update(newUser,id)
#        print(msg)
#
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=400, detail="oops... an error occurred" )
#     print("lkjhgfdsdfghjklnbvcxcvbnm,")
#     return msg

@Expenses_Router.get("/{userId}")
async def get_expenses(userId:int):
  try:
   expenses=await get_expenses(userId)
  except :
    raise HTTPException(status_code=400, detail="oops... an error occurred" )
  return expenses
