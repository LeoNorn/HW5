from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup


shop_router = Router()

@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Фрукты"),
            KeyboardButton(text="Ягоды"),
            KeyboardButton(text="Овощи"),
        ]]

    )
    await message.answer("Выберите категорию: ",
    reply_markup=kb)

@shop_router.message(F.text == "Фрукты")
async def show_frukt(message: types.Message):
    await message.answer("Яблоки, Груши, Бананы")

@shop_router.message(F.text == "Ягоды")
async def show_yagod(message: types.Message):
    await message.answer("Клубника, Арбуз, Малина")

@shop_router.message(F.text == "Овощи")
async def show_ovosh(message: types.Message):
    await message.answer("Огурец, Помидор, Капуста")