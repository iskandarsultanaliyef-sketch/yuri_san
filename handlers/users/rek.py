from aiogram import Router, types
rt = Router()
@rt.message()
async def test(msg: types.Message):
    print(msg.caption_entities)
    if msg.caption_entities:
        turi = msg.caption_entities[0].type in ["url", "mention"]
        if turi:
            await msg.delete()
            await msg.answer(f"reklama tarqatmang {msg.from_user.first_name}")
    elif msg.entities:
            turi = msg.entities[0].type in ["url", "mention"]
            if turi:
                await msg.delete()
                await msg.answer(f"reklama tarqatmang {msg.from_user.first_name}")