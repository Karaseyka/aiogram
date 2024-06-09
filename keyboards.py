from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отправить сообщение менеджеру")]])

contactKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]])
