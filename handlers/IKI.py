from aiogram import types, filters, Router, F, Bot
rt= Router()
# @rt.message(F.text, F.chat.type == "private")
# async def test(msg: types.Message):
#     await msg.answer("siz matn yubordingiz")
#
# @rt.message(F.sticker, F.chat.type == "supergroup")
# async def test(msg: types.Message):
#     await msg.answer("siz sticker yubordingiz")
#
@rt.message(F.animation, F.chat.type == "supergroup")
async def test(msg: types.Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["administrator", "creator"]:
        await msg.answer("siz gif yubordingiz")

@rt.message(F.text, F.chat.type == "supergroup")
async def test(msg: types.Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["administrator", "creator"]:
        await msg.answer("siz gif yubordingiz")

@rt.message(F.audio, F.chat.type == "supergroup")
async def test(msg: types.Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["administrator"]:
        await msg.answer("siz gif yubordingiz")

@rt.message(F.document, F.chat.type.in_(("s", "g")))
# @rt.message(F.document, F.chat.type.in_({"s", "g"}))
async def test(msg: types.Message, bot: Bot):
    user = await bot.get_chat_member(msg.chat.id, msg.from_user.id)
    if user.status in ["creator"]:
        await msg.answer("siz gif yubordingiz")

@rt.message(F.dice, F.chat.type == "private")
async def test(msg: types.Message):
    await msg.answer("siz matn yubordingiz")




















