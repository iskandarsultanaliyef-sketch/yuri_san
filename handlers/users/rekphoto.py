from aiogram import Router, types

rt = Router()

@rt.message()
async def reklama(msg: types.Message):

    entities = msg.entities or []
    caption_entities = msg.caption_entities or []

    if msg.delete_chat_photo:
        print("Guruh rasmi o'chirildi")

    for entity in entities + caption_entities:
        if entity.type in ["url", "text_link"]:
            await msg.delete()
            await msg.answer(
                "Reklama yuborish mumkin emas!"
            )
            return