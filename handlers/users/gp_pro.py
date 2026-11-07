from aiogram import Router, types
from fillters.group import GroupFilter
rt = Router()
@rt.message(GroupFilter())
async def test(msg: types.Message):
    if msg.new_chat_members:
        user = msg.new_chat_members[0]
        user2 = msg.from_user
        n = f"{user.first_name} xush kelibsiz!\n"
        n += f"sizni {user2.first_name} qo'shdi"
        await msg.reply(n)
        if user.id == user2.id:
            await msg.answer(f"{user.first_name} xush kelibsiz!")
            pass
        else:
            user = msg.new_chat_members[0]
            user2 = msg.from_user
            n = f"{user.first_name} xush kelibsiz!\n"
            n += f"sizni {user2.first_name} qo'shdi"
            await msg.reply(n)
            if user.id == user2.id:
                pass

