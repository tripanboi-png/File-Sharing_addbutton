from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["FileSharingBot"]

broadcast = db["broadcast"]


async def add_user(user_id, user_name):
    if not broadcast.find_one({"_id": user_id}):
        broadcast.insert_one({
            "_id": user_id,
            "user_name": user_name
        })


async def delete_user(user_id):
    broadcast.delete_one({"_id": user_id})


async def full_userbase():
    return list(broadcast.find())


async def query_msg():
    return broadcast.find({}, {"_id": 1})
