from pyrogram.types import InlineKeyboardButton
from database.buttons import get_buttons


async def start_button(client):

    buttons = []

    data = await get_buttons()

    for btn in data:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=btn["name"],
                    url=btn["url"]
                )
            ]
        )

    buttons.append(
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs",
                callback_data="help"
            )
        ]
    )

    buttons.append(
        [
            InlineKeyboardButton(
                text="ᴛᴜᴛᴜᴘ",
                callback_data="close"
            )
        ]
    )

    return buttons


async def fsub_button(client, message):

    buttons = []

    data = await get_buttons()

    for btn in data:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=btn["name"],
                    url=btn["url"]
                )
            ]
        )

    try:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="ᴄᴏʙᴀ ʟᴀɢɪ",
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )
    except IndexError:
        pass

    return buttons
