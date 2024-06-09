from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Меню', callback_data="to_main")],
                                      [InlineKeyboardButton(text='Какое-то меню', callback_data="to_main")],
                                      [InlineKeyboardButton(text='Ещё один пункт меню', callback_data="to_main")],
                                       [InlineKeyboardButton(text='И ещё', callback_data="to_main")]])


contactKeyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Поделиться номером", request_contact=True)]])
