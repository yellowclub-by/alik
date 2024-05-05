from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('вы выгледите солидно, не хотите преобрести немного павер энд мативейшен')


@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer('мотивейшн комбо(ямато, мотивейшн и павер, умение котатся на скейте')


@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("да")


@user_router.message(Command('contacts'))
async def contacts(messege: types.Message):
    await messege.answer('нет')


@user_router.message(Command('addresses'))
async def addresses(messege: types.Message):
    await messege.answer('я подумаю')

# @user_router.message()
# async def echo(message: types.Message):
#     await message.answer('бот в разработке, простите мы не можем дать вам POWER')
#     user_text = message.text
#     await message.answer(user_text)
