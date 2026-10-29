from aiogram import Router, types, F, filters

from handlers.users import answer

rt = Router()
import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, types

TOKEN = "TOKENINGIZNI_SHU_YERGA_YOZING"

router = Router()
logging.basicConfig(level=logging.INFO)


@router.message(F.contact)
async def contact(msg: types.Message):
    await msg.answer("contact")

@router.message(F.video)
async def video(msg: types.Message):
    await msg.answer("video")


@router.message(F.audio)
async def audio(msg: types.Message):
    await msg.answer("audio")



@router.message(F.photo)
async def rasim(msg: types.Message):
    await msg.answer("photo")


@router.message(F.voice)
async def golos(msg: types.Message):
    await msg.answer("voice")

@router.message(F.video_note)
async def vd(msg: types.Message):
    await msg.answer("video_note")


@router.message(F.location)
async def l(msg: types.Message):
    await msg.answer("location")

@router.message(F.animation)
async def gif(msg: types.Message):
    await msg.answer("animation")


@router.message(F.sticker)
async def sticker(msg: types.Message):
    await msg.answer("sticker")



@router.message(F.dice)
async def dice(msg: types.Message):
    # Mengambil nilai angka dari dadu yang dilempar[cite: 6]
    await msg.answer(f"javob== {msg.dice.value}")




# students = [
#    "AgACAgIAAxkBAAI3UWrgjb0GbY1sUC6pzh7ppGAk_I1mAAIiIGsbM9sJSx9C0h39_EL7AQADAgADdwADPQQ",
#    "AgACAgIAAxkBAAI3UmrgjchrUsBfvN1tzxlMecN5bw_CAAIjIGsbM9sJS8XLTvlb1s2gAQADAgADdwADPQQ",
#    "AgACAgIAAxkBAAI3U2rgjc7Bli2MFHu3-ezuvuomDqhzAAIkIGsbM9sJS9UPhBoLCWt1AQADAgADdwADPQQ",
# ]
# qoshiqlar = [
#    "CQACAgIAAxkBAAI3jWrgkAbNuIO_sSKe5cntmNPTcYEIAAKLBgACdhPgSe0EntNJMpJbPQQ"
# ]
# @rt.message()
# async def hm(msg: types.Message):
#     if msg.dice:
#         await msg.answer(f"javob== {msg.dice.value}")

   # if msg.contact:
   #
   #    if msg.contact.user_id == msg.from_user.id:
   #       await msg.answer("bu sizniki")
   #    else:
   #       await msg.answer("iltimos o'zingizni nomeringizni bering")
   # if msg.sticker:
   #    await msg.answer(str(msg.sticker.emoji))
   # elif msg.text == "music":
   #    await msg.answer_audio(qoshiqlar[0])
   # # print(msg.photo[-1].file_id)
   # if msg.text == "muhammadiso":
   #    await msg.answer_photo(students[0])
   # elif msg.text == "iskandar" or msg.text == "ibrohim":
   #    await msg.answer_photo(students[1])
   # elif msg.text == "miryoqub":
   #    await msg.answer_photo(students[2])
   # else:
   #    await msg.answer("tur yoqol")
