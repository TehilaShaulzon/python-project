# This is a sample Python script.
from fastapi import FastAPI

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


app = FastAPI()

app.include_router(user, prefix='/Tasks', tags=["Tasks"])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
