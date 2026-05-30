from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import OWNER_ID
from database.admins import (
    add_admin,
    delete_admin,
    get_admins,
    is_admin
)


@Bot.on_message(filters.command("addadmin"))
async def addadmin_cmd(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/addadmin USER_ID"
        )

    try:
        user_id = int(message.command[1])

        await add_admin(user_id)

        await message.reply_text(
            f"✅ Admin ditambahkan\n\n"
            f"ID: <code>{user_id}</code>"
        )

    except Exception as e:
        await message.reply_text(
            f"❌ Error\n<code>{e}</code>"
        )


@Bot.on_message(filters.command("deladmin"))
async def deladmin_cmd(client, message: Message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/deladmin USER_ID"
        )

    try:
        user_id = int(message.command[1])

        if user_id == OWNER_ID:
            return await message.reply_text(
                "❌ Owner tidak bisa dihapus"
            )

        await delete_admin(user_id)

        await message.reply_text(
            f"🗑 Admin dihapus\n\n"
            f"ID: <code>{user_id}</code>"
        )

    except Exception as e:
        await message.reply_text(
            f"❌ Error\n<code>{e}</code>"
        )


@Bot.on_message(filters.command("admins"))
async def admins_cmd(client, message: Message):

    if not await is_admin(message.from_user.id) and message.from_user.id != OWNER_ID:
        return

    data = await get_admins()

    text = "📋 Daftar Admin\n\n"
    text += f"👑 Owner: <code>{OWNER_ID}</code>\n\n"

    for admin in data:
        text += f"• <code>{admin['user_id']}</code>\n"

    await message.reply_text(text)
