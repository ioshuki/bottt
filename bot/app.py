from aiogram import Dispatcher

from bot.middlewares import DbSessionMiddleware
from handlers.commands import router as commands_router
from handlers.messages import router as messages_router
from handlers.callbacks import router as callbacks_router


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.message.middleware(DbSessionMiddleware())
    dp.callback_query.middleware(DbSessionMiddleware())

    dp.include_router(commands_router)
    dp.include_router(messages_router)
    dp.include_router(callbacks_router)

    return dp
