from pydantic import BaseModel, constr, ValidationError, validator, field_validator
from fastapi import FastAPI, Depends, APIRouter


class User(BaseModel):
    name: str
    id: int
