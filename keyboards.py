from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Начать диалог с менеджером")]])

endTalk = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Закончить диалог с менеджером")]])

contactKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]])
