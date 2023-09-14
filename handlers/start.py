from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from text import START_TEXT


start_router = Router()

@start_router.message(Command("start"))
async def hello(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
               IButton(text="Контакты", callback_data="null"),
               IButton(text="О нас", callback_data="null"),
               IButton(text="Наш сайт", url="https://google.com"),
            ],
       ]
    )
    await message.answer(START_TEXT, reply_markup=kb)

