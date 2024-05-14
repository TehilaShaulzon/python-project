from dataAccess.dataAccess import db
from models.users import User

collection = db['users']


async def login(user: User):
    try:
        if(not collection.find_one({"id": user.id})):
            raise EOFError
    except:
        raise "false"
    return f"Hello {user.name}"

async def signUp(user: User):
    try:
      collection.insert_one(user)
    except:
        raise "false"
    return f"Hello {user.name}"

async def update(user: User):
    user=collection.find_one({"id": user.id})
    collection.update_one({"id":user.id},{user})
    return f"Hello {user.name}"

