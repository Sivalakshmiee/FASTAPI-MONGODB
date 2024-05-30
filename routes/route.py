from fastapi import APIRouter
from models.model import User 
from config.config import client 
from schemas.schema import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.get('/')
async def find_all_users():
    return serializeList(client.Product.Product.find())

# @user.get('/{id}')
# async def find_one_user(id):
#     return serializeDict(client.Product.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    client.Product.Product.insert_one(dict(user))
    return serializeList(client.Product.Product.find())

@user.put('/{id}')
async def update_user(id,user: User):
    client.Product.Product.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(client.Product.Product.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(client.Product.Product.find_one_and_delete({"_id":ObjectId(id)}))