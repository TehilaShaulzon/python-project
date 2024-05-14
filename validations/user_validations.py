from fastapi import HTTPException
from models.users import User
from services.userService import collection


def sign_up_check_user(new_user: User):
    print(new_user)
    result = list(collection.find({"name": new_user.name, "password": new_user.password}))
    if len(result) != 0:
        raise HTTPException(status_code=401, detail="name or password is incorrect")
    else:
        return new_user

