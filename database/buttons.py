from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["FileSharingBot"]
buttons = db["buttons"]


async def add_button(text, url):
    buttons.update_one(
        {"_id": text},
        {"$set": {"url": url}},
        upsert=True
    )


async def delete_button(text):
    buttons.delete_one({"_id": text})


async def get_buttons():
    return list(buttons.find())
