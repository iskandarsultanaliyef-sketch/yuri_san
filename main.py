import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from config.settings import BOT_TOKEN
from handlers.users.start import rt as start
from handlers.users.cars import rt as cars
from handlers.users.shops import rt as shops
from handlers.users.ismlar import rt as ismlar
from handlers.users.fruits import rt as fruits
from handlers.users.help import rt as help
from handlers.users.hm import rt as hm
from handlers.users.aloooo import rt as aloooo
from handlers.users.itphoto import rt as itphoto
from handlers.users.phote import rt as phote
from handlers.users.forward import rt as forward
from handlers.users.time import rt as time
from handlers.users.fromid import rt as fromid
from handlers.users.id import rt as id
from handlers.users.akja import rt as akja
from handlers.users.answer import rt as answer
from handlers.users.reply import rt as reply
from handlers.users.delete import rt as delete
from handlers.users.pin import rt as pin
from handlers.users.test import rt as test
dp = Dispatcher()
async def main():
    bot = Bot(BOT_TOKEN)

    dp.include_router(start)
    dp.include_router(cars)
    dp.include_router(shops)
    dp.include_router(ismlar)
    dp.include_router(fruits)
    dp.include_router(help)
    dp.include_router(hm)
    dp.include_router(aloooo)
    dp.include_router(itphoto)
    dp.include_router(phote)
    dp.include_router(forward)
    dp.include_router(time)
    dp.include_router(fromid)
    dp.include_router(id)
    dp.include_router(akja)
    dp.include_router(answer)
    dp.include_router(reply)
    dp.include_router(delete)
    dp.include_router(pin)
    dp.include_router(test)

    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        print("bot ishga tushdi")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("bot to'xtatildi")
    except TelegramNetworkError:
        print("internetga yo'q")
    except TelegramUnauthorizedError:
        print("token xato!")
