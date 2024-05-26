from aiogram import types, Router, F

group_router = Router()
ban = ['пчела', 'кринж', 'пон', 'ааа', 'лягушка'
                                       'болотная', ',', 'даблин']


@group_router.message(F.text)
async def cliner(message: types.Message):
    words_lst = message.text.split(' ')
    for word in words_lst:
        if word.lower() in ban:
            await message.answer(F'соблюдайте правила чата {message.from_user.first_name}')
            await message.delete()
            break
