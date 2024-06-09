from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import keyboards as kb
import db.requests as rq
from Bot import bot

router = Router()

MANAGER_ID = 1052283225


class Send(StatesGroup):
    step1 = State()


@router.message(CommandStart())
async def start(message: Message):
    if await rq.check_user(message.from_user.id):
        await message.answer(f'Добро пожаловать {message.from_user.username}', reply_markup=kb.main)
    else:
        await message.answer("Для регистрации поделитесь номером", reply_markup=kb.contactKeyboard)


@router.message(F.contact)
async def get_contact(message: Message):
    contact = message.contact.phone_number
    tg = message.from_user.id
    await rq.new_user(tg, contact)
    await message.answer("Успешно!!!", reply_markup=kb.main)


@router.message(F.text == "Отправить сообщение менеджеру")
async def to_manager(message: Message, state: FSMContext):
    await state.set_state(Send.step1)
    await message.answer("Введите сообщение")


@router.message(Send.step1)
async def register_name(message: Message, state: FSMContext):
    print(message.chat.id)
    await bot.forward_message(chat_id=MANAGER_ID, from_chat_id=message.from_user.id, message_id=message.message_id)

    await state.clear()


@router.message()
async def for_manager(message: Message):
    if message.from_user.id == MANAGER_ID and message.reply_to_message:
        await bot.send_message(message.reply_to_message.forward_from.id, message.text)


