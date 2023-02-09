from aiogram.utils import executor
from create_bot import dp
from handlers import inline_client_handlers
from handlers import default_handlers


async def on_startup(_):
    print('BOT ONLINE')


default_handlers.register_default_handlers(dp)
inline_client_handlers.register_inline_handlers_client(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
