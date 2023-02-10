from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_location = InlineKeyboardButton('📌Локация остальных кроликов📌', callback_data='location')
button_phone_number = InlineKeyboardButton('☎Номер телефона☎', callback_data='phone_number')
button_email = InlineKeyboardButton('📮Электронная почта📮', callback_data='email')
button_catalog = InlineKeyboardButton('🐰Выбрать кролика🐰', callback_data='catalog')

client_keyboard_commands = InlineKeyboardMarkup(row_width=1)
client_keyboard_commands.add(button_location, button_phone_number, button_email, button_catalog)