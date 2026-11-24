
from aiogram import Router, types, F

rt = Router()

@rt.message(F.chat.type.in_({"group", "supergroup"}), F.forward_origin)
async def delete_forwarded(msg: types.Message):
    try:
        await msg.delete()
    except Exception:
        pass

@rt.message(F.chat.type == "private")
async def say(msg: types.Message):
    if msg.forward_from_chat:
        chat = msg.forward_from_chat

    elif msg.forward_from:
        user = msg.forward_from

    else:
        await msg.answer("a")