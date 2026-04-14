import asyncio

from aiogram import Bot

from bot.app import create_dispatcher
from config.settings import settings
from db.init_db import init_db
from scheduler.jobs import send_daily_plans
from utils.logger import setup_logging


async def scheduler_loop(bot: Bot) -> None:
    while True:
        try:
            await send_daily_plans(bot)
        except Exception as e:
            print(f"[scheduler_loop] {e}")

        await asyncio.sleep(60)


async def main() -> None:
    setup_logging(settings.log_level)

    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = create_dispatcher()

    scheduler_task = asyncio.create_task(scheduler_loop(bot))

    try:
        await dp.start_polling(bot)
    finally:
        scheduler_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
