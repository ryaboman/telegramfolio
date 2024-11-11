from aiogram import Bot
from aiogram.types import Message
from core.keyboards.inline import select_project, business_card
from core.keyboards.keyboard_button import apartment_price_prediction


async def get_class_text(message: Message, bot: Bot):
    await message.answer(f'done')

async def get_start(message: Message, bot: Bot):

    await message.answer(f'Привет <b>{message.from_user.first_name}</b>. '
                         f'Я Бот для демонстрации проектов по Data Science '
                         f'<b>Алексея Рябова</b>')

    await message.answer('Выберите действие', reply_markup=business_card)

    await message.answer('Button', reply_markup=apartment_price_prediction)

    # apartment_price_prediction

async def get_help(message: Message, bot: Bot):
    await message.answer(f'Я Бот для демонстрации проектов по Data Science '
                         f'<b>Алексея Рябова</b>. Используй команду /start для запуска.')

async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил картинку, я сохраню ее себе.')
    file = await  bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'img/' + file.file_id + '.jpg')




