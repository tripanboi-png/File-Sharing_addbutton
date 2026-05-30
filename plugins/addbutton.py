from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from database.admins import is_admin
from database.buttons import add_button, delete_button, get_buttons


@Bot.on_message(filters.command("addbutton"))
async def addbutton_cmd(client, message: Message):
    if not await is_admin(message.from_user.id):
        return

    if len(message.command) < 4:
        return await message.reply_text(
            "Usage:\n/addbutton Nama URL CHAT_ID"
        )

    try:
        name = message.command[1]
        url = message.command[2]
        chat_id = int(message.command[3])

        await add_button(name, url, chat_id)

        await message.reply_text(
            f"✅ Button ditambahkan\n\n"
            f"📌 Nama: {name}\n"
            f"🔗 URL: {url}\n"
            f"🆔 Chat ID: {chat_id}"
        )

    except Exception as e:
        await message.reply_text(f"❌ Error:\n<code>{e}</code>")


@Bot.on_message(filters.command("delbutton"))
async def delbutton_cmd(client, message: Message):
    if not await is_admin(message.from_user.id):
        return

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/delbutton Nama"
        )

    name = message.command[1]

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
