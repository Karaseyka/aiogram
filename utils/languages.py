from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class Rus:
    greet = """
👋Здравствуйте, я бот обратной связи.
Если Вы хотите написать Владимиру Владимировичу, используйте меню ниже 👇"""
    main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Написать",
                                                                       callback_data="st_di")]])
    ask = "Задайте интересующий Вас вопрос или напишите сообщение."
    ans = """
Ваш вопрос записан. 
Если хотите дополнить, нажмите на кнопку ниже."""
    nextStep = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Дополнить",
                                                                           callback_data="add")],
                                                     [InlineKeyboardButton(text="Главное меню",
                                                                           callback_data="to_main")]
                                                     ])


class Eng:
    greet = """
👋Hello, I am a feedback bot. 
If you want to write to Vladimir Vladimirovich, use the menu below 👇"""
    main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Сontact",
                                                                       callback_data="st_di")]])
    ask = "Ask a question or write a message."
    ans = """
Your message is recorded. 
If you want to add more, click on the button below."""
    nextStep = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Add",
                                                                           callback_data="add")],
                                                     [InlineKeyboardButton(text="Main Menu",
                                                                           callback_data="to_main")]
                                                     ])


class Chin:
    greet = """
👋你好，我是一个反馈机器人。 如果您想写信给佛拉基米尔，请使用下面的菜单！👇"""
    main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="联系",
                                                                       callback_data="st_di")],
                                                 [InlineKeyboardButton(text="微信", callback_data="cht")]])
    ask = "问一个问题或写一个信息"
    ans = """
你的信息被记录下来. 如果你想添加更多，点击下面的按钮。
佛拉基米尔还有微信(@viy_24)"""
    nextStep = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="添加",
                                                                           callback_data="add")],
                                                     [InlineKeyboardButton(text="主菜单",
                                                                           callback_data="to_main")]
                                                     ])
