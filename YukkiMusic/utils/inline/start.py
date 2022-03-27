#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝗖𝗈𝗆𝗆𝖺𝗇𝖽𝗌❓"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["𝗖𝗈𝗆𝗆𝖺𝗇𝖽𝗌❓"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["𝗨𝗉𝖽𝖺𝗍𝖾𝗌 📨"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["📨 𝗦𝗎𝗉𝗉𝗈𝗋𝗍"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["𝗨𝗉𝖽𝖺𝗍𝖾𝗌 📨"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["📨 𝗦𝗎𝗉𝗉𝗈𝗋𝗍"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝖡𝖺𝖼𝗄"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["𝗨𝗉𝖽𝖺𝗍𝖾𝗌 📨"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["📨 𝗦𝗎𝗉𝗉𝗈𝗋𝗍"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["𝗨𝗉𝖽𝖺𝗍𝖾𝗌 📨"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["📨 𝗦𝗎𝗉𝗉𝗈𝗋𝗍"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["✚ 𝗔𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ✚"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["𝗢𝗐𝗇𝖾𝗋 🚩"], user_id=OWNER),
                ),
            ]
        )
    else:
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["𝗢𝗐𝗇𝖾𝗋 🚩"], user_id=OWNER
                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons
