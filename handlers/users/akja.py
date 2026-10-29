from aiogram import Router, types, filters
import datetime
rt = Router()
@rt.message()
async def akja(msg: types.Message):
   if msg.text == "aka":
      await msg.answer("uka")
   elif msg.text == "uka":
      await msg.answer("aka")
   else:
      if msg.text == "salom":
         await msg.answer("qalesan")
      else:
         await msg.answer("tushinmadim")
