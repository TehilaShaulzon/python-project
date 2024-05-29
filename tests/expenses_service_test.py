from datetime import datetime

import pytest

from pymongo import MongoClient

from models.expenses import Expenses
from services.expenses_service import get_expenses_by_user_id, collection, update_new_expenses, delete_one_expenses


@pytest.mark.asyncio
async def test_get_expenses_by_user_id():
    """
    Test the function get_expenses_by_user_id.

    This function tests the ability of get_expenses_by_user_id to retrieve all expenses for a specific user from the database.

    Steps:
    1. Create two mock expense records for a user with user_id 3.
    2. Insert the records into the database.
    3. Call the get_expenses_by_user_id function with user_id 3.
    4. Verify the number of returned expenses and check specific fields of the expenses.
    5. Delete the added expenses from the database after the test.
    """
    # Create mock expense records
    mock_expenses_first = {"id": 1, "user_id": 3, "description": "test1", "amount": 100,
                           "date": datetime.strptime("1/5/2020", "%d/%m/%Y")}
    mock_expenses_second = {"id": 2, "user_id": 3, "description": "test2", "amount": 200,
                            "date": datetime.strptime("1/5/2020", "%d/%m/%Y")}

    # Insert records into the database
    collection.insert_one(mock_expenses_first)
    collection.insert_one(mock_expenses_second)

    # Call the function being tested
    expenses = await get_expenses_by_user_id(3)
    print(expenses)

    # Verify the results
    assert len(expenses) == 2
    assert expenses[0]["id"] == 1
    assert expenses[0]["amount"] == 100
    assert expenses[1]["id"] == 2
    assert expenses[1]["amount"] == 200

    # Clean up the database
    collection.delete_many({"user_id": 3})


@pytest.mark.asyncio
async def test_update_new_expenses():
    """
    Test the function update_new_expenses.

    This function tests the ability of update_new_expenses to correctly update an existing expense record in the database.

    Steps:
    1. Create a mock expense object for the update.
    2. Create an original expense object to simulate the current state in the database.
    3. Call the update_new_expenses function to update the expense.
    4. Verify that the updated fields are correct.
    5. Restore the original expense object in the database.
    """
    # Create mock expense object for the update
    mock_expenses = Expenses(id=5, user_id=26, description="updated test2", amount=200,
                             date=datetime.strptime("1/5/2020", "%d/%m/%Y"))
    # Create original expense object to simulate the current state in the database
    original_expenses = Expenses(id=5, user_id=26, description="test expenses", amount=150,
                                 date=datetime.strptime("4/5/2022", "%d/%m/%Y"))

    # Call the function being tested
    updated_expense = await update_new_expenses(mock_expenses, "5", 26)

    # Verify the results
    assert updated_expense.amount == 200
    assert updated_expense.id == 5
    assert updated_expense.description != "test expenses"

    # Restore the original expense object in the database
    await update_new_expenses(original_expenses, "5", 26)
