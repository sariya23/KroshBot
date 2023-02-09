from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


button_show_commands = InlineKeyboardButton('Я ОБУЧЕН КОМАНДАМ(тыкни)', callback_data='show_commands')

client_keyboard_start = InlineKeyboardMarkup()
client_keyboard_start.add(button_show_commands)