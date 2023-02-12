from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_back = InlineKeyboardButton('Назад', callback_data='back')


button_belichij = InlineKeyboardButton('🐇Беличий\nкарлик🐇', callback_data='breed0 belichij')
button_germelin = InlineKeyboardButton('🐇Гермелин🐇', callback_data='breed0 germelin')
button_karlikovyj_baran = InlineKeyboardButton('🐇Карликовый\nбаран🐇', callback_data='breed0 karlikovyj-baran')
button_minor = InlineKeyboardButton('🐇Менор🐇', callback_data='breed0 minor')
button_minilop = InlineKeyboardButton('🐇МиниЛоп🐇', callback_data='breed0 minilop')
button_niderlandskij = InlineKeyboardButton('🐇Нидерландский🐇', callback_data='breed0 niderlandskij')
button_xotot = InlineKeyboardButton('🐇Хотот🐇', callback_data='breed0 xotot')
button_cvetnoj_karlik = InlineKeyboardButton('🐇Цветной карлик🐇', callback_data='breed0 cvetnoj-karlik')
button_url = InlineKeyboardButton('📁Подробнее о породах📁', url='https://tsarskiykrolik.com/blog/')

client_keyboard_breeds = InlineKeyboardMarkup(row_width=3)
client_keyboard_breeds.add(button_belichij, button_germelin, button_xotot)
client_keyboard_breeds.add(button_minor, button_minilop, button_niderlandskij)
client_keyboard_breeds.add(button_karlikovyj_baran, button_cvetnoj_karlik)
client_keyboard_breeds.add(button_url)
