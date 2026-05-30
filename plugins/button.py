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

join_buttons = []

for btn in data:
    join_buttons.append(
        InlineKeyboardButton(
            text=btn["name"],
            url=btn["url"]
        )
    )

if join_buttons:
    buttons.append(join_buttons)

buttons.append(
    [
        InlineKeyboardButton(
            text="COBA LAGI",
            url=f"https://t.me/{client.username}?start={message.command[1]}"
        )
    ]
)

return buttons
