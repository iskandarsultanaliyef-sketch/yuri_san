
from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("shops"))
async def shops(msg: types.Message):

    await msg.answer("1. BMW M5 10000000$\n"
        "2. Mercedes-Benz AMG 111111111$\n"
        "3. Audi RS7 1222221$\n"
        "4. Lamborghini Huracan 111111$\n"
        "5. Ferrari SF90 7867876$\n"
        "6. Bugatti Chiron 45678$")
