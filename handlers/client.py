from aiogram import types, Dispatcher
from create_bot import bot
from keyboards.client_kb import client_keyboard_start
from keyboards.client_kb import client_keyboard_commands
from aiogram.dispatcher.filters import Text


async def empty(message: types.Message):
    """An empty handler does not work on commands"""
    await bot.send_message(message.from_user.id,
                           f'Я кролик-бот. Меня зовут Крош. '
                           f'Я реагирую только на определенные команды, прям как настоящий кролик',
                           reply_markup=client_keyboard_start)


async def show_commands(callback: types.CallbackQuery):
    """Show inline keyboard command"""
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


async def send_email(callback: types.CallbackQuery):
    """Send email"""
    await bot.send_message(callback.from_user.id, 'Пиши сюда:\ntsarskiy_krolik@mail.ru')
    await callback.answer()


def register_handlers_client(dp: Dispatcher):
    """The function registers handlers"""
    dp.register_callback_query_handler(show_commands, Text(startswith=('show')))
    dp.register_callback_query_handler(send_address_shop, Text(startswith=('location')))
    dp.register_callback_query_handler(send_phone_number, Text(startswith=('phone_number')))
    dp.register_callback_query_handler(send_email, Text(startswith=('email')))
    dp.register_message_handler(empty)
