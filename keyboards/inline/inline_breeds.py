from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_back = InlineKeyboardButton('Назад', callback_data='back')


button_belichij = InlineKeyboardButton('🐇Беличий\nкарлик🐇', callback_data='breed belichij')
button_germelin = InlineKeyboardButton('🐇Гермелин🐇', callback_data='breed germelin')
button_karlikovyj_baran = InlineKeyboardButton('🐇Карликовый\nбаран🐇', callback_data='breed karlikovyj-baran')
button_minor = InlineKeyboardButton('🐇Менор🐇', callback_data='breed minor')
button_minilop = InlineKeyboardButton('🐇МиниЛоп🐇', callback_data='breed minilop')
button_niderlandskij = InlineKeyboardButton('🐇Нидерландский🐇', callback_data='breed niderlandskij')
button_xotot = InlineKeyboardButton('🐇Хотот🐇', callback_data='breed xotot')
button_cvetnoj_karlik = InlineKeyboardButton('🐇Цветной карлик🐇', callback_data='breed cvetnoj-karlik')
button_url = InlineKeyboardButton('📁Подробнее о породах📁', url='https://tsarskiykrolik.com/blog/')

client_keyboard_breeds = InlineKeyboardMarkup(row_width=3)
client_keyboard_breeds.add(button_belichij, button_germelin, button_xotot)
client_keyboard_breeds.add(button_minor, button_minilop, button_niderlandskij)
client_keyboard_breeds.add(button_karlikovyj_baran, button_cvetnoj_karlik)
client_keyboard_breeds.add(button_url)
