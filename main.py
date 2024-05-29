"""
main.py

This script sets up and runs a FastAPI application with routes for managing users, expenses, income, and data visualization.

Modules Imported:
    - uvicorn: ASGI server for serving the FastAPI application.
    - bson.ObjectId: ObjectId for MongoDB document identification.
    - fastapi.FastAPI: The main FastAPI class for creating the application instance.
    - controllers.expenses_controller.Expenses_Router: Router for managing expenses-related endpoints.
    - controllers.income_controller.Income_Router: Router for managing income-related endpoints.
    - controllers.userController.User_Router: Router for managing user-related endpoints.
    - controllers.visualization_controller.visualization_Router: Router for managing data visualization endpoints.
    - data_access.data_access.db: Database access module for interacting with the database.

Usage:
    Run the script using the command `python main.py` or by pressing Shift+F10 in an IDE like PyCharm.

    Example:
        To start the server, navigate to the project directory and run:
        $ uvicorn main:app --host 127.0.0.1 --port 8080

Routes:
    - /Users: User management endpoints (e.g., creating, updating, deleting users).
    - /Expenses: Expense management endpoints (e.g., adding, updating, retrieving expenses).
    - /Income: Income management endpoints (e.g., adding, updating, retrieving income).
    - /visualization: Data visualization endpoints.


"""
import uvicorn
from bson import ObjectId
from fastapi import FastAPI

from app.controllers.expenses_controller import Expenses_Router
from app.controllers.income_controller import Income_Router
from app.controllers.user_controller import User_Router
from app.controllers.visualization_controller import visualization_Router
from app.services.service_data_access import db

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

app.include_router(User_Router, prefix='/Users', tags=["Users"])
app.include_router(Expenses_Router, prefix='/Expenses', tags=["Expenses"])
app.include_router(Income_Router, prefix='/Income', tags=["Income"])
app.include_router(visualization_Router, prefix="/visualization")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     uvicorn.run("main:app", host="127.0.0.1", port=8080)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
