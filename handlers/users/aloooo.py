
from aiogram import Router, types, F

rt = Router()


@rt.message(F.video)
async def video(msg: types.Message):
    await msg.answer("video")


@rt.message(F.text)
async def text(msg: types.Message):
    await msg.answer("text")


@rt.message(F.sticker)
async def sticker(msg: types.Message):
    await msg.answer("sticker")


@rt.message(F.contact)
async def contact(msg: types.Message):
    await msg.answer("contact")


@rt.message(F.dice)
async def dice(msg: types.Message):
    await msg.answer("dice")


@rt.message(F.document)
async def document(msg: types.Message):
    await msg.answer("document")


@rt.message(F.location)
async def location(msg: types.Message):
    await msg.answer("location")


@rt.message(F.venue)
async def venue(msg: types.Message):
    await msg.answer("venue")


@rt.message(F.voice)
async def voice(msg: types.Message):
    await msg.answer("voice")


@rt.message(F.audio)
async def audio(msg: types.Message):
    await msg.answer("audio")








