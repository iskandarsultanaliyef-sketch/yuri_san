import datetime
import random
from aiogram import Router, types

rt = Router()

@rt.message()
async def say(msg: types.Message):
    if msg.forward_from_chat :
        chat = msg.forward_from_chat
        await msg.answer(f"Kanal\nNomi: "
                         f"{chat.title}\nID: "
                         f"{chat.id}")

    elif msg.forward_from :
        rt = msg.forward_from
        await msg.answer(f"Botmi: {rt.is_bot}\n"
                         f"Nomi: {rt.full_name}\n"
                         f"ID: {rt.id}")

    else:
        await msg.answer("mmmmmmm")