from aiogram import Router, types

rt = Router()

@rt.message()
async def reklama(msg: types.Message):

    for entity in msg.entities or []:
        if entity.type == "text_mention":
            if entity.user.id < 0:
                await msg.delete()
                await msg.answer("🚫 Reklama mumkin emas!")
                return