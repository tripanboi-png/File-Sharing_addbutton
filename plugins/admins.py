from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["FileSharingBot"]
admins = db["admins"]


async def is_admin(user_id):
    return admins.find_one({"user_id": user_id}) is not None


async def add_admin(user_id):
    if not admins.find_one({"user_id": user_id}):
        admins.insert_one({"user_id": user_id})


async def delete_admin(user_id):
    admins.delete_one({"user_id": user_id})


async def get_admins():
    return list(admins.find())
