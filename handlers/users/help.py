from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("help"))
async def help(msg: types.Message):
    await msg.answer("sizga nima yordam beraolaman")
    n = "mendagi barcha kamandalar:\n"
    n += "/cars\n"
    n += "/shops\n"
    n += "/ismlar\n"
    n += "/fruits\n"
    n += "/reply\n"
    n += "/photo\n"
    n += "/dice\n"
    n += "/delete\n"
    n += "/answer\n"
    n += "/pin\n"
    n += "/alo\n"
    n += "/aloooo\n"
    n +="/vaqt\n"
    n += "/akja\n"
    n += "/say\n"
    n += "/it\n"
    n += "/aloooo\n"
    n += "/hm\n"
    n +="/vd\n"
    n += "/video\n"
    n += "/rasim\n"
    n += "/audio\n"
    n += "/golos\n"
    n += "/dice\n"
    n += "/contact\n"
    n += "/vd\n"
    n += "/text\n"
    n += "/stiker\n"
    n += "/l\n"
    # n += "video\n"
    # n += "dice\n"
    # n += "stiker\n"
    # n += "text\n"
    # n += "audio\n"
    await msg.answer(n)


