
from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("cars"))
async def cars(msg: types.Message):
    await msg.answer("1. BMW M5\n"
        "2. Mercedes-Benz AMG\n"
        "3. Audi RS7\n"
        "4. Lamborghini Huracan\n"
        "5. Ferrari SF90\n"
        "6. Bugatti Chiron")
