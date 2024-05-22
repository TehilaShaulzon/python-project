import pytest

from models.users import User
from services.userService import collection, signUp, login


@pytest.mark.asyncio
async def test_sign_up_user():
    """
    Test the signUp function and the login function.

    This function tests the ability of signUp to create a new user in the database and the ability of login to authenticate the user.

    Steps:
    1. Create a mock user object for the new user.
    2. Call the signUp function to add the user to the database.
    3. Call the login function to authenticate the newly created user.
    4. Verify that the user exists in the database.
    5. Clean up the database by deleting the mock user.
    """
    # Create mock user object for the new user
    mock_user = User(id=1, name="test_user", password="111111", email="test@j.com")

    # Call the signUp function to add the user to the database
    await signUp(mock_user)

    # Call the login function to authenticate the newly created user
    result = await login("test_user", "111111")
    print(result)

    # Verify that the user exists in the database
    assert len(list(collection.find({"name": "test_user", "password": "111111"}))) == 1

    # Clean up the database by deleting the mock user
    collection.delete_one({"name": "test_user", "password": "111111"})
