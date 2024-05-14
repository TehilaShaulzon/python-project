from fastapi import HTTPException

from dataAccess.dataAccess import db
from models.users import User

collection = db['users']
user_id = (collection.find({}, { 'id': 1}).sort('id', -1)[0])["id"]

async def login(name,password):
    try:
        print(name + " " + password)
        result = list(collection.find({"name": name, "password": password}))
        if len(result) == 0:
            raise HTTPException(status_code=401, detail="you are not registered")
        else:
            return f"hello {name} your id {result[0]}"
    except Exception as e:
        raise e


async def signUp(user: User):
    try:
      global user_id
      user_id+=1
      user.id =user_id
      collection.insert_one(user.dict())
    except :
        raise HTTPException(status_code=401, detail="an error occurred")
    return f"Hello {user.name}"

async def update(new_user: User,user_id):
    try:
       print(user_id)
       print(new_user.id)
       if user_id!= str(new_user.id):
           raise HTTPException(status_code=401, detail="the id you insert is incorrect")
       result=list(collection.find({"id": new_user.id}))
       print("qweeeeee")
       print(result)
       if len(result)==0:
        raise HTTPException(status_code=401, detail="this Id is not found")
       else:
        collection.update_one({"id": user_id}, {"$set": new_user.dict()})
    except Exception as e:
         raise e

    return new_user
