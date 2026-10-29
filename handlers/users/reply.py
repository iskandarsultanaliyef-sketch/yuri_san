from aiogram import Router, types , filters
rt = Router()
@rt.message(filters.Command("reply"))
async def reply(msg: types.Message):

    await msg.reply("mana reply yozdim")

