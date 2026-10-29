
import random
from aiogram import Router, types
from aiogram.filters import Command

rt = Router()

r = [
    "https://media.printler.com/media/photo/179657.jpg?rmode=crop&width=425&height=600",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3gukHnykS996L0L6X7Du88HuHMWA787Wsp3RdPx0a8A&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-0A_8Uht6pww4TOXgnjwGfVK4mSBgP3m2ZUw34JCDIw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7UJdmFcnZBcxcHJCXIdFFr3ozka34uoUNU94rQQEmdA&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM83yr8ndd9FZZ5peuoN9PoYh-BD7F4IulwmOUP9YA3g&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHdvd3Pu03ttxITtg6MJCUV5AguMkU-UnR-PuMTnYGpg&s=10"
]

@rt.message(Command("it"))
async def it(msg: types.Message):
    await msg.answer_photo(random.choice(r))
