from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher.filters import Text

from keyboards.client_kb import client_keyboard_start
from keyboards.client_kb import client_keyboard_commands
from keyboards.client_kb import client_keyboard_breeds

from Parser_class import Parser


current_keyboard_level = 0
#
KEYBOARD_LEVELS = {
    0: (client_keyboard_start, 'Я кролик-бот. Меня зовут Крош. Я реагирую только на определенные команды, прям как настоящий кролик'),
    1: (client_keyboard_commands, 'Вот что я умею'),
    2: (client_keyboard_breeds, 'Нас много, но все мы разные')
}
#
# KEYBOARD_LEVELS = {
#     0: empty,
#
# }


async def empty(message: types.Message):
    """An empty handler does not work on commands"""
    await bot.send_message(message.from_user.id,
                           f'Я кролик-бот. Меня зовут Крош. '
                           f'Я реагирую только на определенные команды, прям как настоящий кролик',
                           reply_markup=client_keyboard_start)


async def show_commands(callback: types.CallbackQuery):
    """Send inline keyboard command"""
    global current_keyboard_level
    current_keyboard_level = 1

    await bot.send_message(callback.from_user.id, 'Вот что я умею', reply_markup=client_keyboard_commands)
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
    global current_keyboard_level
    current_keyboard_level = 2

    await bot.send_message(callback.from_user.id,
                           'Нас много, но все мы разные',
                           reply_markup=client_keyboard_breeds)


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
                           f'Это большинство кроликов породы {callback.data.split()[1]}.'
                           f'Их больше на нашем сайте: https://tsarskiykrolik.com/',
                           reply_markup=client_keyboard_breeds)


async def back(callback: types.CallbackQuery):
    """Send prev. inline keyboard"""
    await bot.send_message(callback.from_user.id, KEYBOARD_LEVELS[current_keyboard_level - 1][1], reply_markup=KEYBOARD_LEVELS[current_keyboard_level - 1][0])


def register_handlers_client(dp: Dispatcher):
    """The function registers handlers"""
    dp.register_callback_query_handler(show_commands, Text(startswith=('show')))
    dp.register_callback_query_handler(send_address_shop, Text(startswith=('location')))
    dp.register_callback_query_handler(send_phone_number, Text(startswith=('phone_number')))
    dp.register_callback_query_handler(send_email_address, Text(startswith=('email')))
    dp.register_callback_query_handler(show_catalog, Text(startswith=('catalog')))
    dp.register_callback_query_handler(show_picked_breed, Text(startswith=('breed')))
    dp.register_callback_query_handler(back, Text(startswith=('back')))
    dp.register_message_handler(empty)
