from aiogram import Router, filters,  types
rt = Router()
@rt.message(filters.Command("pin"))
async def pin(msg: types.Message):
    await msg.pin()
