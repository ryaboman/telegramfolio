from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start, get_photo, get_help, get_button_price_apartment_prediction
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command
from aiogram import F
from core.utils.commands import set_commands
from core.handlers.viewer_projects_ml import select_projects, get_project_text_classification
from core.handlers.viewer_projects_ml import selector_actions, get_project_age_recognition
from core.handlers.viewer_projects_ml import get_project_digit_recognition, get_project_audio_transcription
from core.utils.statesform import StepsViewProjects
from core.handlers.viewer_projects_ml import get_class_text, get_digit_from_img, cancel_state_fsm
from core.handlers.viewer_projects_ml import get_prediction_price_apartment

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.callback_query.register(select_projects, F.data == 'view_projects')
    dp.callback_query.register(selector_actions, F.data == 'backward')

    dp.callback_query.register(get_project_text_classification, F.data == 'text_classification')
    dp.callback_query.register(get_project_age_recognition, F.data == 'age_recognition')
    dp.callback_query.register(get_project_digit_recognition, F.data == 'digit_recognition')
    dp.callback_query.register(get_project_audio_transcription, F.data == 'audio_transcription')
    dp.callback_query.register(get_button_price_apartment_prediction, F.data == 'price_apartment_prediction')

    dp.message.register(get_class_text, ~F.text.startswith('/'),
                        StepsViewProjects.TC_WAIT_TEXT)
    dp.message.register(get_digit_from_img, ~F.text.startswith('/'),
                        StepsViewProjects.NR_WAIT_IMG)

    dp.message.register(get_prediction_price_apartment, F.web_app_data)

    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(cancel_state_fsm, Command(commands=['cancel']))
    dp.message.register(get_help, Command(commands=['help']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
