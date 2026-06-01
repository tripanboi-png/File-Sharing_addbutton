# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton
from database.buttons import get_buttons


async def start_button(client):

    buttons = []

    data = await get_buttons()

    join_buttons = []

    for btn in data:
        join_buttons.append(
            InlineKeyboardButton(
                text=btn["name"],
                url=btn["url"]
            )
        )

    # 2 tombol atas, sisanya ke bawah
    if len(join_buttons) >= 2:
        buttons.append(join_buttons[:2])

        for btn in join_buttons[2:]:
            buttons.append([btn])

    elif len(join_buttons) == 1:
        buttons.append([join_buttons[0]])

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


async def fsub_button(client, message):

    buttons = []

    data = await get_buttons()

    join_buttons = []

    for btn in data:
        join_buttons.append(
            InlineKeyboardButton(
                text=btn["name"],
                url=btn["url"]
            )
        )

    # 2 tombol atas, sisanya ke bawah
    if len(join_buttons) >= 2:
        buttons.append(join_buttons[:2])

        for btn in join_buttons[2:]:
            buttons.append([btn])

    elif len(join_buttons) == 1:
        buttons.append([join_buttons[0]])

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
