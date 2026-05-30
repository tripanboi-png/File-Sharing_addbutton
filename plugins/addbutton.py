import re

from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from database.admins import is_admin
from database.buttons import add_button, delete_button, get_buttons


@Bot.on_message(filters.command("addbutton"))
async def addbutton_cmd(client, message: Message):

    if not await is_admin(message.from_user.id):
        return

    text = message.text

    match = re.match(
        r'/addbutton\s+"(.+)"\s+(@[\w\d_]+)',
        text
    )

    if not match:
        return await message.reply_text(
            'Usage:\n/addbutton "Nama Button" @username'
        )

    try:

        name = match.group(1)
        username = match.group(2)

        chat = await client.get_chat(username)

        await add_button(
            name=name,
            url=f"https://t.me/{username.replace('@', '')}",
            chat_id=chat.id
        )

        await message.reply_text(
            f"✅ Button ditambahkan\n\n"
            f"📌 Nama: {name}\n"
            f"🔗 Username: {username}\n"
            f"🆔 Chat ID: {chat.id}"
        )

    except Exception as e:
        await message.reply_text(
            f"❌ Error\n\n<code>{e}</code>"
        )


@Bot.on_message(filters.command("delbutton"))
async def delbutton_cmd(client, message: Message):

    if not await is_admin(message.from_user.id):
        return

    text = message.text.split(maxsplit=1)

    if len(text) < 2:
        return await message.reply_text(
            "Usage:\n/delbutton Nama Button"
        )

    name = text[1]

    await delete_button(name)

    await message.reply_text(
        f"🗑 Button {name} dihapus"
    )


@Bot.on_message(filters.command("buttons"))
async def buttons_cmd(client, message: Message):

    if not await is_admin(message.from_user.id):
        return

    data = await get_buttons()

    if not data:
        return await message.reply_text(
            "Belum ada button."
        )

    text = "📋 Daftar Button:\n\n"

    for btn in data:

        text += (
            f"• {btn['name']}\n"
            f"  {btn['url']}\n"
            f"  {btn.get('chat_id', 'Tidak ada')}\n\n"
        )

    await message.reply_text(text)
