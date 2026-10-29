
from aiogram import Router, filters, types
rt = Router()
@rt.message(filters.Command("fruits"))
async def fruits(msg: types.Message):
    await msg.answer("1. BMW m5\n"
        "2. Mercedes-Benz amg\n"
        "3. Audi RS7\n"
        "4. Lamborghini hurum\n"
        "5. Ferrari sf60\n"
        "6. Bugatti chirom")
