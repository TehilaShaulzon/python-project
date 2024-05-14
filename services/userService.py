from dataAccess.dataAccess import db
from models.users import User

collection = db['users']
user_id =0

async def login(user: User):
    try:
        collection.find_one({"name": user.name,"password":user.password})
    except Exception as e:
        raise e
    return f"Hello {user.name}"

async def signUp(user: User):
    try:
      global user_id
      user_id+=1
      user.id =user_id
      collection.insert_one(user.dict())
    except :
        raise ValueError("")
    return f"Hello {user.name}"

async def update(new_user: User,user_id):
    try:
       if(not collection.find_one({"id": user_id})):
           raise EOFError
       collection.update_one({"id": user_id}, {"$set": new_user.dict()})
    except:
         raise ValueError("error!!!")

    return collection.find_one({"id":user_id})















