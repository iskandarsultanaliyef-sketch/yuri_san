import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import (
    TelegramNetworkError,
    TelegramUnauthorizedError,
)

from config.settings import BOT_TOKEN

# Handler/Routerlarni import qilish
from handlers.users.aareklama import rt as aareklama
from handlers.users.rek import rt as rek
from handlers.users.useer import rt as useer
from handlers.users.rekphoto import rt as rekphoto
from handlers.users.reklama import rt as reklama
from handlers.users.start import rt as start
from handlers.users.cars import rt as cars
from handlers.users.shops import rt as shops
from handlers.users.ismlar import rt as ismlar
from handlers.users.fruits import rt as fruits
from handlers.users.gp_pro import rt as gp_pro
from handlers.users.hm import rt as hm
from handlers.users.help import rt as help
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
    # aiogram 3.x uchun Bot obyektini yaratish
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    # Routerlarni ulash (kerakli routerlarni izohdan chiqaring)
    dp.include_routers(
        # start,
        aareklama,
        # reklama,
        # useer,
        # rekphoto,
        # rek,
        # cars,
        # shops,
        # ismlar,
        # fruits,
        # gp_pro,
        # help,
        # hm,
        # aloooo,
        # itphoto,
        # phote,
        # forward,
        # time,
        # fromid,
        # id,
        # akja,
        # answer,
        # reply,
        # delete,
        # pin,
        # test
    )

    # Eski kutilayotgan buyruqlarni tozalash (eski soʻrovlar birdan kelib tushmasligi uchun)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Konsolda xatolik va loglarni ko'rish uchun
    try:
        print("Bot ishga tushdi...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")
    except TelegramNetworkError:
        print("Internet aloqasi yo'q!")
    except TelegramUnauthorizedError:
        print("BOT_TOKEN xato kiritilgan!")