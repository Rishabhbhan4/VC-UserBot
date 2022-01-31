from config import HNDLR
from pyrogram import Client, filters
from pyrogram.types import Message
from UserBot.Rishabh.custfilters import (
    admin_fliter
)

@Client.on_message(filters.command(["pin", "pn"], prefixes=f"{HNDLR}")
    & admin_fliter
)
async def pin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.pin()


@Client.on_message(filters.command(["unpin", "up"], prefixes=f"{HNDLR}")
    & admin_fliter
)
async def unpin(_, message: Message):
    if not message.reply_to_message:
        return
    await message.reply_to_message.unpin()
