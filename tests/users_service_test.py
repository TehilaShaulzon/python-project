import pytest

from models.users import User
from services.userService import collection, signUp, login


@pytest.mark.asyncio
async def test_sign_up_user():

    mock_expenses_first = User(id= 1, name="test_user" ,password="111111",email="test@j.com")

    result=await signUp(mock_expenses_first)
    result=await login("test_user","111111")
    print(result)
    assert len(list(collection.find({"name":"test_user","password":"111111"})))==1


    collection.delete_one({"name":"test_user","password":"111111"})
