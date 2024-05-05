import asyncio
from aiogram import Bot, Dispatcher

TOKEN = '6996688346:AAEF_p6ejIWYrH9yR_pTvgroSgqMVlWYPAM'

bot = Bot(token=TOKEN)
dp = Dispatcher()

from handles.user_privat import user_router

dp.include_router(user_router)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
