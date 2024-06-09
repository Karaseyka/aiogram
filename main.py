import asyncio

import aiogram
from aiogram import Bot, Dispatcher
from heandlers import router

from db.model import async_main
from Bot import bot


async def main():
    await async_main()
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
