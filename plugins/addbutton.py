from pyrogram import filters
from pyrogram.types import Message

from bot import Bot


@Bot.on_message(filters.command("buttons"))
async def buttons_cmd(client, message: Message):
    await message.reply_text("Fitur sedang dibuat")
