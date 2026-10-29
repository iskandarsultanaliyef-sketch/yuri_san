from aiogram import Router, types, filters
rt = Router()
@rt.message(filters.Command("answer"))
async def answer(msg: types.Message):

    await msg.answer("oddiy javob")

