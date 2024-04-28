import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = '6996688346:AAEV26orIvxBI-Gq9e6GgVbF3EHBmH1xk7I'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('вы выгледите солидно, не хотите преобрести немного павер энд мативейшен')


@dp.message()
async def echo(message: types.Message):
    await message.answer('бот в разработке, простите мы не можем дать вам POWER')
    user_text = message.text
    await message.answer(user_text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
