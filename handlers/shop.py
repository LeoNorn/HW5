import db.shopdb
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from db.shopdb import get_product


shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Купить Фрукты"),
            KeyboardButton(text="Купить Ягоды"),
            KeyboardButton(text="Купить Овощи"),
        ]]

    )
    await message.answer("Выберите категорию: ",
                         reply_markup=kb)

@shop_router.message(F.text == "Купить Фрукты")
async def show_frukt(message: types.Message):
    products = get_product()
    for pr in get_product():
        await message.answer(pr[1])



@shop_router.message(F.text == "Купить Ягоды")
async def show_yagod(message: types.Message):
    products = get_product()
    for pr in get_product():
        await message.answer(pr[2])


@shop_router.message(F.text == "Купить Овощи")
async def show_ovosh(message: types.Message):
    products = get_product()
    for pr in get_product():
        await message.answer(pr[3])