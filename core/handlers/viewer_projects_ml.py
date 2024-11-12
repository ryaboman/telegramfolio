import os

from aiogram import Bot
from aiogram.types import CallbackQuery, InputMediaPhoto, FSInputFile
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsViewProjects
from aiogram.types import Message
from apps.text_classification import model_text_classification as model
from apps.digit_recognition import model_digit_recognition as model_digit
from apps.apartment_price_prediction import model_price_apartment_prediction as model_price
from core.keyboards.inline import select_project, business_card
from aiogram.types import ReplyKeyboardRemove
import json

async def cancel_state_fsm(message:Message, bot: Bot, state: FSMContext):
    await state.clear()
    await message.answer('Ок, состояние сброшено.', reply_markup=ReplyKeyboardRemove())
    await message.answer(f'Выберите действие', reply_markup=business_card)


async def selector_actions(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Выберите действие', reply_markup=business_card)
    await call.answer()

async def select_projects(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text(f'Выберите проект для ознакомления:', reply_markup=select_project)
    await call.answer()

async def get_project_text_classification(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Выбран проект <b>классификатор текста сообщений</b>. '
                         f'Возможные классы сообщений: нормальный, оскорбительный, угроза, непристойный. '
                         f'Введите текст:')
    await state.set_state(StepsViewProjects.TC_WAIT_TEXT)
    await call.answer()

async def get_project_age_recognition(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Проект еще в разработке!')
    # await state.set_state(StepsViewProjects.TC_WAIT_TEXT)
    await call.message.answer(f'Выберите проект для ознакомления:', reply_markup=select_project)
    await call.answer()

async def get_project_digit_recognition(call: CallbackQuery, bot: Bot, state: FSMContext):
    await call.message.answer(f'Пришли мне картинку с цифрой или нарисуй цифру на картинке, '
                              f'которую я тебе сейчас пришлю')
    img = FSInputFile(r'img/pattern.jpg')
    await bot.send_photo(call.message.chat.id, img)
    await state.set_state(StepsViewProjects.NR_WAIT_IMG)
    # await call.message.answer(f'Проект еще в разработке!')
    # await call.message.answer(f'Выберите проект для ознакомления:', reply_markup=select_project)
    await call.answer()

async def get_project_audio_transcription(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Проект еще в разработке!')
    # await state.set_state(StepsViewProjects.TC_WAIT_TEXT)
    await call.message.answer(f'Выберите проект для ознакомления:', reply_markup=select_project)
    await call.answer()

async def get_class_text(message: Message, bot: Bot):
    print(message.text)
    if len(message.text) > 300:
        await message.answer('Не могу обработать, текст слишком длинный. '
                             'Максимальная длинна 300 символов')
        return 0
    mark_text = model.get_predict(message.text)
    print(mark_text)
    if mark_text[0]:
        await message.answer('Текс классифицирован как <b>нормальный</b>.')
    if mark_text[1]:
        await message.answer('Текс классифицирован как <b>оскорбительный</b>.')
    if mark_text[2]:
        await message.answer('Текс классифицирован как <b>угроза</b>.')
    if mark_text[3]:
        await message.answer('Текс классифицирован как <b>непристойный</b>.')

    await message.answer('Еще текст? Используйте /cancel для отмены.')

async def get_digit_from_img(message:Message, bot: Bot):
    await message.answer(f'Отлично. Ты отправил картинку, я начинаю распознавать цифру.')
    file = await bot.get_file(message.photo[-1].file_id)
    base_path = 'img/rec_digit/'
    file_name = file.file_id + '.jpg'
    full_path = base_path + file_name

    await bot.download_file(file.file_path, full_path)

    digit = model_digit.get_predict(full_path)
    await message.answer(f'Распознанная цифра: <b>{digit}</b>')
    # удалить картинку
    os.remove(full_path)

    await message.answer('Еще картинка с цифрой? Используйте /cancel для отмены.')

def get_description_of_parameters(data):
    output_string = ''
    for key, value in data.items():
        if key == 'total_area':
            output_string += '\n' + f'Общая площадь: {value}'
        elif key == 'living_area':
            output_string += '\n' + f'Жилая площадь: {value}'
        elif key == 'kitchen_area':
            output_string += '\n' + f'Площадь кухни: {value}'
        elif key == 'rooms':
            if value == 0:
                output_string += '\n' + f'Количество комнат: студия'
            else:
                output_string += '\n' + f'Количество комнат: {value}'
        elif key == 'balcony':
            if value == 0:
                output_string += '\n' + f'Наличие балкона: нет'
            else:
                output_string += '\n' + f'Наличие балкона: да'
        elif key == 'logie':
            if value == 0:
                output_string += '\n' + f'Наличие лоджии: нет'
            else:
                output_string += '\n' + f'Наличие лоджии: да'
        elif key == 'bathroom':
            output_string += '\n' + f'Количество санузлов: {value}'
        elif key == 'renovation':
            if value == 0:
                output_string += '\n' + f'Ремонт: без ремонта'
            elif value == 1:
                output_string += '\n' + f'Ремонт: косметический'
            elif value == 2:
                output_string += '\n' + f'Ремонт: евроремонт'
            elif value == 3:
                output_string += '\n' + f'Ремонт: дизайнерский'
        elif key == 'gas_supply':
            if value == 0:
                output_string += '\n' + f'Газоснабжение: нет'
            else:
                output_string += '\n' + f'Газоснабжение: да'
        elif key == 'floor':
            output_string += '\n' + f'Этаж: {value}'
        elif key == 'floors_total':
            output_string += '\n' + f'Этажность дома: {value}'
        elif key == 'passenger_elevator':
            if value == 0:
                output_string += '\n' + f'Пассажирский лифт: нет'
            else:
                output_string += '\n' + f'Пассажирский лифт: да'
        elif key == 'service_elevator':
            if value == 0:
                output_string += '\n' + f'Грузовой лифт: нет'
            else:
                output_string += '\n' + f'Грузовой лифт: да'
        elif key == 'year':
            output_string += '\n' + f'Год постройки дома: {value}'
        elif key == 'type_of_building':
            if value == 0:
                output_string += '\n' + f'Тип дома: нет информации'
            elif value == 1:
                output_string += '\n' + f'Тип дома: кирпичный'
            elif value == 2:
                output_string += '\n' + f'Тип дома: панельный'
            elif value == 3:
                output_string += '\n' + f'Тип дома: монолитный'
            elif value == 4:
                output_string += '\n' + f'Тип дома: блочный'
            elif value == 5:
                output_string += '\n' + f'Тип дома: монолитно-кирпичный'
        elif key == 'region':
            if value == 0:
                output_string += '\n' + f'Район: нет информации'
            elif value == 1:
                output_string += '\n' + f'Район: Автозаводский'
            elif value == 2:
                output_string += '\n' + f'Район: Советский'
            elif value == 3:
                output_string += '\n' + f'Район: Сормовский'
            elif value == 4:
                output_string += '\n' + f'Район: Московский'
            elif value == 5:
                output_string += '\n' + f'Район: Нижегородский'
            elif value == 6:
                output_string += '\n' + f'Район: Ленинский'
            elif value == 7:
                output_string += '\n' + f'Район: Канавинский'
            elif value == 8:
                output_string += '\n' + f'Район: Приокский'
    return output_string


async def get_prediction_price_apartment(message: Message, bot: Bot):
    data = json.loads(message.web_app_data.data)

    output_string = ''
    for key, value in data.items():
        output_string += '\n' + f'{key}: {value}'
    output_string = get_description_of_parameters(data)
    await message.answer(f"Получили следующие параметры квартиры: {output_string}")

    prediction = model_price.get_predict([data])
    await message.answer(f"Рыночная стоимость Вашей квартиры: {prediction} ₽")
