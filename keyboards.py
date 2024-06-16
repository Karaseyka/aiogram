from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

language = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Русский")],
                                         [KeyboardButton(text="English")],
                                         [KeyboardButton(text="中文")]], resize_keyboard=True)

adm = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Закончить ввод")]], resize_keyboard=True)

fl = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="CSV файл с пользователями")]])
def mes_to_admin(name, id):
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Ответить пользователю: " + str(name),
                                                                       callback_data=f"touser_{id}")]])
