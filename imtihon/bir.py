from aiogram import F, Router, types , filters

rt = Router()


@rt.message(filters.Command("aniqla"))
async def aniqla(msg: types.Message):
    user = msg.from_user

    if user.username:
        await msg.answer(f"username: @{user.username}")
    elif user.first_name:

        await msg.answer(f"First Name: {user.first_name}")
    else:
        await msg.answer(f"Last Name: {user.last_name}")

