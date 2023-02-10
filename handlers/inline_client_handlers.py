from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text

from keyboards.inline.inline_breeds import client_keyboard_breeds
from keyboards.inline.inline_commands import client_keyboard_commands

from Parser_class import Parser


# current_keyboard_level = 0
#
# STACK = []
#
# KEYBOARD_LEVELS = {
#     # 0: (client_keyboard_start, 'Я кролик-бот. Меня зовут Крош. Я реагирую только на определенные команды, прям как настоящий кролик'),
#     # 1: (client_keyboard_commands, 'Вот что я умею'),
#     2: (client_keyboard_breeds, 'Нас много, но все мы разные')
# }

english_to_russian = {
    'belichij': 'Беличий карлик',
    'germelin': 'Гермелин',
    'karlikovyj-baran': 'Карликовый барон',
    'minor': 'Менор',
    'minilop': 'МиниЛоп',
    'niderlandskij': 'Нидерландский',
    'xotot': 'Хотот',
    'cvetnoj-karlik': 'Цветной карлик'
}


async def empty(message: types.Message):
    """An empty handler does not work on commands"""
    await bot.send_message(message.from_user.id,
                           f'Неизвестная команда(. Чтобы увидеть мои возможности '
                           f'пропиши /start',)


async def command_start(callback: types.CallbackQuery):
    """Triggers by command /start
    Send inline keyboards with commands"""
    await bot.send_message(callback.from_user.id,
                           f'Вот что я умею',
                           reply_markup=client_keyboard_commands)
    await callback.answer()


async def send_address_shop(callback: types.CallbackQuery):
    """Send address of the shop"""
    await bot.send_message(callback.from_user.id, 'Мы с братьями и сестрами тусуемся здесь:\n'
                                                  'Московская область Деревня Тарычево, ул. Яблоневая 7-В')
    await callback.answer()


async def send_phone_number(callback: types.CallbackQuery):
    """Send phone number"""
    await bot.send_message(callback.from_user.id, 'Звони сюда:\n'
                                                  '+79252215934')
    await callback.answer()


async def send_email_address(callback: types.CallbackQuery):
    """Send email address"""
    await bot.send_message(callback.from_user.id, 'Пиши сюда:\ntsarskiy_krolik@mail.ru')
    await callback.answer()


async def show_catalog(callback: types.CallbackQuery):
    """Send inline keyboard with breeds of the rabbits"""
    await bot.send_message(callback.from_user.id,
                           'Нас много, но все мы разные',
                           reply_markup=client_keyboard_breeds)
    await callback.answer()


async def show_picked_breed(callback: types.CallbackQuery):
    """Send inline keyboard with breeds of rabbits"""
    data = Parser().parse(callback.data.split()[1])

    for i in data:
        if not i.discount_price:
            await bot.send_photo(callback.from_user.id, i.img_url,
                                 f'🐇Пушистик породы🐇: <b>{i.breed}</b>\n'
                                 f'💵Стоимость счастья💵: {i.old_price}\n'
                                 f'🔬Подробнее🔬: {i.more_info}',
                                 parse_mode='html')
        else:
            await bot.send_photo(callback.from_user.id, i.img_url,
                                 f'🐇Пушистик породы🐇: <b>{i.breed}</b>\n'
                                 f'💵Стоимость по скидке💵: {i.discount_price}\n'
                                 f'<b>⌛СКИДКА ПРОДЛИТСЯ ЕЩЕ⌛</b>: {i.time_to_disc_end}\n'
                                 f'🔬Подробнее🔬: {i.more_info}',
                                 parse_mode='html')
    await callback.answer()
    await bot.send_message(callback.from_user.id,
                           f'Это большинство кроликов породы {english_to_russian[callback.data.split()[1]]}.'
                           f'Их больше на нашем сайте: https://tsarskiykrolik.com/',
                           reply_markup=client_keyboard_breeds)


def register_inline_handlers_client(dp: Dispatcher):
    """The function registers handlers"""
    dp.register_callback_query_handler(command_start, Text(startswith=('show_commands')))
    dp.register_callback_query_handler(send_address_shop, Text(startswith=('location')))
    dp.register_callback_query_handler(send_phone_number, Text(startswith=('phone_number')))
    dp.register_callback_query_handler(send_email_address, Text(startswith=('email')))
    dp.register_callback_query_handler(show_catalog, Text(startswith=('catalog')))
    dp.register_callback_query_handler(show_picked_breed, Text(startswith=('breed')))
    dp.register_message_handler(empty)
