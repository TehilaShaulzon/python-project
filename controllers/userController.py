import uvicorn
from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from pydantic import BaseModel,constr, ValidationError, validator, field_validator
from models.users import User
from services.userService import login, signUp, update
from validations.user_validations import sign_up_check_user

User_Router = APIRouter()


@User_Router.post("/login/")
async def login_user(name,password):
    try:
      print(name+" "+password)
      await login(name,password)
    except Exception as e:
        raise e
    return f"Hello {name}"

@User_Router.post("/signUp/")
async def add_user(user: User=Depends(sign_up_check_user)):
    try:
        print(user)
        await signUp(user)
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"

@User_Router.put("/{id}", response_model=User)
async def update_user(newUser: User,id):
    try:
       result=await update(newUser,id)
    except Exception as e:
        print(e)
        raise e
    return result

