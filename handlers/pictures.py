from aiogram import types, Router
from aiogram.filters import Command
import random


picture_router = Router()



@picture_router.message(Command("photo"))
async def send_random_photo(message: types.Message):
    file = types.FSInputFile("images/7uO4PqZj2X4.jpg")
    file2 = types.FSInputFile("images/94uyj0_ATBU.jpg")
    file3 = types.FSInputFile("images/1644976612_29-fikiwiki-com-p-kartinki-pro-brata-39.jpg")
    file4 = types.FSInputFile("images/B7hvQusB4B4.jpg")
    file5 = file, file2, file3, file4
    random_photo = random.choice(file5)
    await message.answer_photo(random_photo)