import uvicorn

from fastapi import FastAPI, Depends, APIRouter
from fastapi import  HTTPException
from fastapi.encoders import jsonable_encoder

from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,constr, ValidationError, validator, field_validator

from models.users import User
from services.userService import login, signUp, update

User_Router = APIRouter()





@User_Router.post("/login/")
async def login_user(user: User):
    try:
        if(not login(user)):
            raise EOFError
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"

@User_Router.post("/signUp/")
async def add_user(user: User):
    try:
        signUp(user)
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return f"Hello {user.name}"

@User_Router.put("/{id}", response_model=User)
async def update_user(user: User):
    try:
       update(user)
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return "true"

