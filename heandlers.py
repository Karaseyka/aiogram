from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import CommandStart
import keyboards as kb
from bot import bot
import utils.languages as lang
import data.requestCSV as fl

router = Router()

ADMIN_ID = 949887888


class Send(StatesGroup):
    step1 = State()


@router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(f'Вы можете только отвечать на сообщения', reply_markup=kb.fl)
    else:
        users = await fl.read_users()
        if message.from_user.username not in users:
            users.append(message.from_user.username)
        await fl.write_user(users)
        await message.answer(f'Please select your language before starting', reply_markup=kb.language)


@router.message(F.text == "Русский")
async def lang_rus(message: Message, state: FSMContext):
    await state.update_data(language=lang.Rus)
    data = await state.get_data()
    await message.answer(data["language"].greet, reply_markup=data["language"].main)


@router.message(F.text == "English")
async def lang_eng(message: Message, state: FSMContext):
    await state.update_data(language=lang.Eng)
    data = await state.get_data()
    await message.answer(data["language"].greet, reply_markup=data["language"].main)


@router.message(F.text == "中文")
async def lang_chin(message: Message, state: FSMContext):
    await state.update_data(language=lang.Chin)
    data = await state.get_data()
    await message.answer(data["language"].greet, reply_markup=data["language"].main)


@router.callback_query(F.data.startswith("st_di"))
async def write_to_admin(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.set_state(Send.step1)
    del_kb = types.ReplyKeyboardRemove()
    await callback.message.answer(data["language"].ask, reply_markup=del_kb)


@router.message(Send.step1)
async def to_manager(message: Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(ADMIN_ID, message.text,
                           reply_markup=kb.mes_to_admin(message.from_user.username, message.from_user.id))
    await message.answer(data["language"].ans, reply_markup=data["language"].nextStep)


@router.callback_query(Send.step1, F.data.startswith("add"))
async def add_to_manager(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(data["language"].ask)


@router.callback_query(F.data.startswith("cht"))
async def ans_from_admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(photo=FSInputFile("data/photo.jpeg"))


@router.callback_query(Send.step1, F.data.startswith("to_main"))
async def to_main_menu(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await state.clear()
    await state.update_data(language=data["language"])
    await callback.message.answer(data["language"].greet, reply_markup=data["language"].main)


class Admin(StatesGroup):
    step1 = State()


@router.callback_query(F.data.startswith("touser"))
async def ans_from_admin(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Вводите сообщения (для прекращения отправки сообщений нажмите кнопку 'Закончить ввод')",
        reply_markup=kb.adm)
    await state.update_data(user=callback.data.split("_")[1])
    await state.set_state(Admin.step1)


@router.message(F.text == "Закончить ввод")
async def end_mes_to_user(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f'Вы можете только отвечать на сообщения')


@router.message(Admin.step1)
async def to_user(message: Message, state: FSMContext):
    data = await state.get_data()
    await bot.send_message(int(data["user"]), message.text)


@router.message(F.text == "CSV файл с пользователями")
async def csv_with_users(message: Message, state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        await message.reply_document(document=FSInputFile('data/users.csv'))
