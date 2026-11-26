

from aiogram import types, Router, F
from aiogram.filters import Filter
from config import settings

rt = Router()

ADMINS = settings.ADMINS


@rt.message(F.chat.type.in_(("supergroup", "group")))
async def reklama_hand(msg: types.Message):

    if str(msg.from_user.id) in ADMINS:
        return
    if msg.entities or msg.caption_entities:
            if msg.entities:
                for reklama in msg.entities:
                    if reklama.type in ["mention", "url"]:
                        await msg.delete()
                        if msg.from_user.username:
                            await msg.answer(f"@{msg.from_user.username} reklama tarqatma")
                        else:
                            await msg.answer(f"{msg.from_user.first_name} reklama tarqatma!")
            else:
                if msg.caption_entities:
                    for reklama in msg.caption_entities:
                        if reklama.type in ["mention", "url"]:
                            await msg.delete()
                            if msg.from_user.username:
                                await msg.answer(f"@{msg.from_user.username} reklama tarqatma")
                            else:
                                await msg.answer(f"{msg.from_user.first_name} reklama tarqatma!")


                                break






































