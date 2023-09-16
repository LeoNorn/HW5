import asyncio
import logging
from handlers.start import start_router
from handlers.info import info_router
from handlers.pictures import picture_router
from handlers.shop import shop_router
from bot import bot, dp
from handlers.question import questions_router

async def main():
    dp.include_routers(start_router, info_router, picture_router, shop_router, questions_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
