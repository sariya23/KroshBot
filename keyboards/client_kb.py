from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Start inline
button_show_commands = InlineKeyboardButton('Я ОБУЧЕН КОМАНДАМ(тыкни)', callback_data='show_commands')

client_keyboard_start = InlineKeyboardMarkup()
client_keyboard_start.add(button_show_commands)

# Commands
button_location = InlineKeyboardButton('Локация остальных кроликов', callback_data='location')
button_phone_number = InlineKeyboardButton('Номер телефона', callback_data='phone_number')

client_keyboard_commands = InlineKeyboardMarkup(row_width=1)
client_keyboard_commands.add(button_location, button_phone_number)
