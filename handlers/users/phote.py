
import random
from aiogram import Router, types
from aiogram.filters import Command

rt = Router()

r = [
    "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=639974981915992",
    "https://content.imageresizer.com/images/memes/Cute-Cat-meme-4xgqu.jpg",
    "https://www.meowbox.com/cdn/shop/articles/Screen_Shot_2024-03-15_at_10.53.41_AM.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7NToXLZt7U9KNrS6CrfOoOjgGK-eleOtW8RegwWo_jA&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREDSRfV2vWDSoyeT2AAwIgR8msWdSSn5i2nOVltWdpNA&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXjKvcvsdavlWxdHy2ROHlAK4SDHXq8ObFRMsr3s7gtQ&s=10"
]

@rt.message(Command("photo"))
async def photo(msg: types.Message):
    await msg.answer_photo(random.choice(r))
