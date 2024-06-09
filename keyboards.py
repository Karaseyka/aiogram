from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Меню')],
                                     [KeyboardButton(text='Какое-то меню')],
                                     [KeyboardButton(text='Ещё один пункт меню'),
                                      KeyboardButton(text='И ещё')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

contactKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]])
