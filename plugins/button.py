# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
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

    if FORCE_SUB_CHANNEL:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="ᴄʜᴀɴɴᴇʟ",
                    url=client.invitelink
                )
            ]
        )

    if FORCE_SUB_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text="ɢʀᴏᴜᴘ",
                    url=client.invitelink2
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
