import ftplib

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('вы выгледите солидно, не хотите преобрести немного павер энд мативейшен')


@user_router.message(F.text.lower() == 'меню')
@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer('мотивейшн комбо(ямато, мотивейшн и павер, умение котатся на скейте')


@user_router.message(F.text.lower() == 'о нас')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer("да")


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(messege: types.Message):
    await messege.answer('нет')


@user_router.message(F.text.lower() == 'адреса')
@user_router.message(Command('addresses'))
async def addresses(messege: types.Message):
    await messege.answer('я подумаю')


# @user_router.message(F.text)
@user_router.message(F.photo)
async def echo(message: types.Message):
    await message.answer('сработал магический фильтр ешкеррееееееееееееееее')

# @user_router.message(F.text.lower() == 'доставка')
# async def echo(message: types.Message):
#     await message.answer('сам забирай пидор')


# @user_router.message(F.text.lower().contains('доставк'))
# async def echo(message: types.Message):
#     await message.answer('да хозяин')


# @user_router.message(F.text.startswith('как'))
# async def echo(message: types.Message):
#     await message.answer('никак')

# @user_router.message(F.text.endswith('?'))
# async def echo(message: types.Message):
#     await message.answer('да я сам не знаяю и вообще я ещкере бой эээээээээээээээээ')

# @user_router.message(F.text.startswith('как').endswith('?'))
# async def echo(message: types.Message):
#     await message.answer('да я сам не знаяю и вообще я ещкере бой эээээээээээээээээ')

# @user_router.message( (F.text.lower().contains('стоимост')) | (F.text.lower().contains('цен')) )
# async def echo(message: types.Message):
#     await message.answer('для тебя бесплатно')
