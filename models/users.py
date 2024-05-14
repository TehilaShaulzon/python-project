from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi import FastAPI, Depends, APIRouter


class User(BaseModel):
    id: int
    name: str
    password: str
    email: str
