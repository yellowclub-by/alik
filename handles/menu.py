from aiogram import types, Router, F
from aiogram.types import FSInputFile

menu_router = Router()


@menu_router.message(F.text.lower() == 'мотивейшн комбо')
async def combo(message: types.Message):
    photo = FSInputFile('img\menu\combo.jpeg')
    await message.answer_photo(photo, caption='''<b>комбо</b>

(ямато мотвейшен и павер а также умение кататся на скейте) 

<b>стоит 2000000 красных орбов</b>''')


@menu_router.message(F.text.lower() == 'пиццаданте')
async def pizza(message: types.Message):
    photo = FSInputFile('img\menu\pizza.jpg')
    await message.answer_photo(photo, caption='''<b>вкусная пица</b>
     
и мой брат в подарак 

<b>всеголишь за 15 тысяч красных орбов</b>''')


@menu_router.message(F.text.lower() == 'плашь вергил')
async def pizza(message: types.Message):
    photo = FSInputFile('img\menu\pl_Verg.jpg')
    await message.answer_photo(photo, caption='''<b>мотивационае одияния

за 500 тысяч красных орбов</b>''')


@menu_router.message(F.text.lower() == 'павер')
async def pizza(message: types.Message):
    photo = FSInputFile('img\menu\Vergil_i_need_more_power.jpg')
    await message.answer_photo(photo, caption='''<b>надо больше силы!!!!!!

стоимасть 100 тысяч красных орбав</b>''')
