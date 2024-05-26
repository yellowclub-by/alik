from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню'),
            KeyboardButton(text='о нас'),
        ],
        [
            KeyboardButton(text='контакты'),
            KeyboardButton(text='адреса')
        ]
    ],
    resize_keyboard= True,
    input_field_placeholder='мур'
)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='мотивейшн комбо'),
            KeyboardButton(text='пиццаДанте')
        ],
        [
            KeyboardButton(text='плашь Вергил'),
            KeyboardButton(text='павер')
        ]
    ],
    resize_keyboard= True,
    input_field_placeholder='мур мур'
)
