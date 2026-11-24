from aiogram import Router, types, filters
from aiogram.fsm.context import FSMContext
from aaaaa.anketa_state import AnketaState

rt = Router()
from aiogram import F, filters, types
from aiogram.fsm.context import FSMContext


@rt.message(filters.Command("anketa"))
async def anketa(msg: types.Message, state: FSMContext):
    await msg.answer("Bizga qanday rangdagi mashina bermoqchisiz?")
    await state.set_state(AnketaState.rang)

@rt.message(AnketaState.rang)
async def rang_xato(msg: types.Message):
    await msg.answer("Iltimos, rang nomini faqat harflar bilan kiriting ")

@rt.message(AnketaState.rang)
async def rang(msg: types.Message, state: FSMContext):
    if msg.text:
        await state.update_data(rang=msg.text)
        await msg.answer("Mashina modelini kiriting ")
        await state.set_state(AnketaState.model)
    else:
        await msg.answer("Iltimos, mashina rangini matn ko'rinishida kiriting!")


@rt.message(AnketaState.model)
async def model(msg: types.Message, state: FSMContext):
    if msg.text:
        await state.update_data(model=msg.text)
        data = await state.get_data()
        rang_nomi = data['rang']

        await msg.answer(f"Sizning {rang_nomi} {msg.text} narxini kiriting:")
        await state.set_state(AnketaState.narx)
    else:
        await msg.answer("Iltimos, mashina modelini matn ko'rinishida kiriting!")


@rt.message(AnketaState.narx)
async def narx(msg: types.Message, state: FSMContext):
    if msg.text:

        toza_narx = msg.text.replace("$", "").strip()

        if toza_narx.isdigit():
            await state.update_data(narx=toza_narx)
            data = await state.get_data()

            n = "Tugadi! Sizning mashinangiz:\n\n"
            n += f" Rangi: {data['rang']}\n"
            n += f" Modeli: {data['model']}\n"
            n += f"Narxi: {data['narx']}$"

            await msg.answer(n)
            await state.clear()
        else:
            await msg.answer("Narxni faqat raqam (yoki $ belgisi) bilan kiriting!")
    else:
        await msg.answer("Iltimos, narxni matn ko'rinishida kiriting!")