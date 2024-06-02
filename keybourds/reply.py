from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = KeyboardButton(text='назад')

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
        ],
        [
            back_btn
        ]
    ],
    resize_keyboard= True,
    input_field_placeholder='мур мур'
)
