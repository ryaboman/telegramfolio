from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

select_project = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Классификатор текста',
            callback_data='text_classification'
        )
    ],
    [
        InlineKeyboardButton(
            text='Определение возраста человека по фото',
            callback_data='age_recognition'
        )
    ],
    [
        InlineKeyboardButton(
            text='Распознать цифру на картинке',
            callback_data='digit_recognition'
        )
    ],
    [
        InlineKeyboardButton(
            text='Транскрибация аудио',
            callback_data='audio_transcription'
        )
    ],
    [
        InlineKeyboardButton(
            text='« Назад',
            callback_data='backward'
        )
    ]
])

business_card = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Сайт-визитка Алексея Рябова',
            web_app=WebAppInfo(url='https://aleksey-ryabov.ru')
        )
    ],
    [
        InlineKeyboardButton(
            text='Связаться с Алексеем Рябовым',
            url='t.me/ryaboman'
        )
    ],
    [
        InlineKeyboardButton(
            text='Перейти к проектам',
            callback_data='view_projects'
        )
    ]
])
