from aiogram import Router, types , filters
rt = Router()
@rt.message(filters.Command("delete"))
async def delete(msg: types.Message):


    await msg.delete()

