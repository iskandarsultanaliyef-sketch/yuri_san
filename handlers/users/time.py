from aiogram import Router, types, filters
import datetime

rt = Router()

@rt.message(filters.Command("vaqt"))
async def vaqt(msg: types.Message):
   sana = msg.date + datetime.timedelta(hours=5)

   await msg.answer(
       f"yil : {sana.year}\n"
       f"Oy : {sana.month}\n"
       f"kun : {sana.day}\n"
       f"s : {sana.hour} : {sana.minute} :m  {sana.minute} : s@ {sana.second} \n"
   )
