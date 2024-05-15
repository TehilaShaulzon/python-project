# This is a sample Python script.

import uvicorn
from bson import ObjectId
from fastapi import FastAPI

from controllers.expenses_controller import Expenses_Router
from controllers.userController import User_Router
from dataAccess.dataAccess import db

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

app.include_router(User_Router, prefix='/Users', tags=["Users"])
app.include_router(Expenses_Router, prefix='/Expenses', tags=["Expenses"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     uvicorn.run("main:app", host="127.0.0.1", port=8080)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
