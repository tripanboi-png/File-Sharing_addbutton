from pymongo import MongoClient
from config import MONGO_URI, OWNER_ID

client = MongoClient(MONGO_URI)

db = client["FileSharingBot"]
admins = db["admins"]


async def is_admin(user_id):

    if user_id == OWNER_ID:
        return True

    return admins.find_one(
        {"user_id": user_id}
    ) is not None


async def add_admin(user_id):

    if user_id == OWNER_ID:
        return

    if not admins.find_one(
        {"user_id": user_id}
    ):
        admins.insert_one(
            {"user_id": user_id}
        )


async def delete_admin(user_id):

    if user_id == OWNER_ID:
        return

    admins.delete_one(
        {"user_id": user_id}
    )


async def get_admins():
    return list(admins.find())
