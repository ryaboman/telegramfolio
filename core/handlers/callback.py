from aiogram import Bot
from aiogram.types import CallbackQuery
from core.keyboards.inline import select_project
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsViewProjects
from aiogram.types import Message

async def select_projects(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Выберите проект для ознакомления:', reply_markup=select_project)
    await call.answer()

async def get_project_text_classification(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Выбранный проект - классификатор текста. '
                         f'Возможные классы текста: '
                         f'Введите текст:')
    await state.set_state(StepsViewProjects.TC_WAIT_TEXT)
    await call.answer()
