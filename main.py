import asyncio
import random
from dotenv import load_dotenv
from os import getenv
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

load_dotenv()
token = getenv("TOKEN")
bot = Bot(token=token)

dp = Dispatcher()



@dp.message(Command("start"))
async def hello(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"Привет {message.from_user.first_name}",
    )

@dp.message(Command("myinfo"))
async def info(message: types.Message):
    print(message.from_user)
    await message.answer(
        f"Ваш id: {message.from_user.id}, Ваш first_name: {message.from_user.first_name}, "
        f"Ваш username: {message.from_user.username}",
    )

@dp.message(Command("picture"))
async def send_random_photo(message: types.Message):
    file = types.FSInputFile("images/richard.jpg")
    file2 = types.FSInputFile("images/emamen.jpg")
    file3 = types.FSInputFile("images/hm.jpg")
    file4 = types.FSInputFile("images/medic.jpg")
    file5 = types.FSInputFile("images/obamna.jpg")
    file6 = types.FSInputFile("images/papich.jpg")
    file7 = types.FSInputFile("images/rock.jpg")
    file8 = types.FSInputFile("images/skuf.jpg")
    file9 = file, file2, file3, file4, file5, file6, file7, file8
    random_photo = random.choice(file9)
    await message.answer_photo(random_photo)



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())