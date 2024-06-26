import asyncio
from aiogram import Bot, Dispatcher

TOKEN = '6996688346:AAEF_p6ejIWYrH9yR_pTvgroSgqMVlWYPAM'

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()

from handles.user_privat import user_router
from handles.user_group import group_router
from handles.menu import menu_router
dp.include_router(user_router)
dp.include_router(menu_router)
dp.include_router(group_router)



async def main():
    print('Start')
    await dp.start_polling(bot)


asyncio.run(main())
