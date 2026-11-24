from aiogram import types, filters, Router
import requests
url = "https://api.api-ninjas.com/v1/celebrity"
headers = {
    'X-Api-Key': 'CrDpVnmBQRYLCs6Qb5B4O0jT8LE89lgFhYF0ikwv'
}
rt= Router()
@rt.message()
async def test(msg: types.Message):
    try:
        params = {
            'name': msg.text,
        }
        response = requests.get(url=url, headers=headers, params=params)
        n = response.json()
        javob = "futbolchi haqida qisqacha malumot:\n"
        javob += f"ism: {n[0]["name"]}\n"
        javob += f"tug'ilgan sana: {n[0]["birthday"]}"
        await msg.answer(javob)
    except:
        await msg.answer("bunaqa futbolchi mavjud emas")
