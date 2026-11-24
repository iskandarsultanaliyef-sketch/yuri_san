from aiogram import types, Router
import requests

url = "https://api.api-ninjas.com/v1/soccerclubs"

headers = {
    "X-Api-Key": "API_KEY"
}

rt = Router()


@rt.message()
async def test(msg: types.Message):
    try:
        params = {
            "team": msg.text
        }

        response = requests.get(
            url=url,
            headers=headers,
            params=params
        )

        n = response.json()

        javob = "⚽ Futbol klubi haqida qisqacha ma'lumot:\n"
        javob += f"Klub nomi: {n[0]['name']}\n"
        javob += f"Mamlakat: {n[0].get('country', 'Maʼlumot yoʻq')}\n"

        await msg.answer(javob)

    except:
        await msg.answer("Bunday futbol klubi mavjud emas")