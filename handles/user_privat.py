from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keybourds import reply, inline

user_router = Router()


@user_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer('<b>вы выгледите солидно</b>, не хотите преобрести немного павер энд мативейшен',
                         reply_markup=reply.start_kb, )


@user_router.message(F.text.lower() == 'меню')
@user_router.message(Command('menu'))
async def menu(message: types.Message):
    await message.answer('pawer!!!!',
                         reply_markup=reply.menu_kb)


@user_router.message(F.text.lower() == 'о нас')
@user_router.message(Command("about"))
async def about(message: types.Message):
    await message.answer(" мы такието такието делаем тота тота вот наши средства связи если будут вопросы переходите и спрашивате у них",
                         reply_markup=inline.links_kb)


@user_router.message(F.text.lower() == 'контакты')
@user_router.message(Command('contacts'))
async def contacts(messege: types.Message):
    await messege.answer('идутся сроительные работы в случае возникновения вопросов обрашайтесь к админу в разделе о нас')


@user_router.message(F.text.lower() == 'адреса')
@user_router.message(Command('addresses'))
async def addresses(messege: types.Message):
    await messege.answer('вот лакации которые есть',
                         reply_markup=inline.addresses_kb())


@user_router.callback_query(F.data.lower().startswith('addresses'))
async def addresses_types(callback: types.CallbackQuery):
    query = callback.data.split('_')[1]
    if query == "1":
        await callback.message.answer('http://surl.li/brqefa')
    elif query == "2":
        await callback.message.answer('http://surl.li/pkhohm')
    await callback.answer()

@user_router.message(F.text.lower() == 'назад')
async def back(message: types.Message):
    await message.answer('главное меню',
                         reply_markup=reply.start_kb)

# @user_router.message(F.text)
# @user_router.message(F.photo)
# async def echo(message: types.Message):
#     await message.answer('сработал магический фильтр ешкеррееееееееееееееее')

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
