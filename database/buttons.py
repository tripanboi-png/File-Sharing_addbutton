from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)

db = client["FileSharingBot"]
buttons = db["buttons"]


async def add_button(name, url, chat_id=None):
    buttons.insert_one(
        {
            "name": name,
            "url": url,
            "chat_id": chat_id
        }
    )


async def delete_button(name):
    buttons.delete_one(
        {
            "name": name
        }
    )


async def get_buttons():
    return list(buttons.find())


async def get_join_buttons():
    return list(
        buttons.find(
            {
                "chat_id": {
                    "$exists": True,
                    "$ne": None
                }
            }
        )
    )
