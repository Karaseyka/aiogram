from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import keyboards as kb
import db.requests as rq

router = Router()


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
    await message.answer("Успешно!!!")
