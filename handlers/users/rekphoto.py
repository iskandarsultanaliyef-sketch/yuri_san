from aiogram import Router, types

rt = Router()


@rt.message()
async def test(msg: types.Message):
    print(msg.delete_chat_photo)
    if msg.delete_chat_photo:
        turi = msg.delete_chat_photo[0].type in ["url", "mention"]
        if turi:
            await msg.delete()
            await msg.answer(f"reklama tarqatmang {msg.from_user.first_name}")
