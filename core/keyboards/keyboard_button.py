from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

apartment_price_prediction = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Рассчитать',
            web_app=WebAppInfo(url='https://telegram.ryaboman.ru/apartment-price-prediction')
        )
    ]
], resize_keyboard=True, one_time_keyboard=True,
    input_field_placeholder='Стоимость квартиры ↓')
