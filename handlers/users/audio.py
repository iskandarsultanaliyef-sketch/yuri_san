from aiogram import Router, types, F
rt = Router()
@rt.message(F.audio)
async def audio(msg: types.Message):
   await msg.answer("siz musiqa yubordingiz")

