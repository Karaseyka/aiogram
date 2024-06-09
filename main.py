import asyncio

import aiogram
from aiogram import Bot, Dispatcher
from heandlers import router
from db.model import async_main


async def main():
    await async_main()
    bot = Bot(token='7428837088:AAHAaoxx-_AAQ_M8kFibEk5d5qDeBHBn6sk')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
