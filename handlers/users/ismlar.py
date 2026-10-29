
from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("ismlar"))
async def ismlar(msg: types.Message):
    await msg.answer("1. BMW\n"
        "2. Mercedes-Benz\n"
        "3. Audi\n"
        "4. Lamborghini\n"
        "5. Ferrari\n"
        "6. Bugatti")
