from aiogram import Router, types, F
rt = Router()
@rt.message(F.sticker)
async def stik(msg: types.Message):
   await msg.answer("siz stik yubordingiz")