from aiogram import Router, types, filters

rt = Router()


@rt.message(filters.Command("aloooo"))
async def aloooo(msg: types.Message):



    if msg.from_user.first_name :
        ism = msg.from_user.first_name
    else:
        ism = "yoooqqqq"
    if msg.from_user.last_name :
        familya = msg.from_user.last_name
    else:
        familya = "yoooqqqqqq"
    if msg.from_user.username :
        username = f"@{msg.from_user.username}"
    else:
        usernamea = "yoooqqqqqq"

    await msg.answer(f"ism :: {ism}")
    await msg.answer(f"FAMILYA :: {familya}")
    await msg.answer(f"USERNAMEA :: {usernamea}")
    await msg.answer(f" username :: {username}")

























