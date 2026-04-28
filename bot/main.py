import asyncio
import logging

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from bot.app import create_dispatcher
from config.settings import settings
from db.init_db import init_db
from scheduler.jobs import send_daily_plans, send_reminders
from utils.logger import setup_logging

logger = logging.getLogger(__name__)


async def main() -> None:
    setup_logging(settings.log_level)
    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = create_dispatcher()

    # Планировщик
    scheduler = AsyncIOScheduler()

    # Каждую минуту проверяем, не пора ли отправить план
    scheduler.add_job(
        send_daily_plans,
        trigger=IntervalTrigger(minutes=1),
        args=[bot],
        id="daily_plans",
        max_instances=1,
        coalesce=True,
    )

    # Каждые 6 часов проверяем неактивных пользователей
    scheduler.add_job(
        send_reminders,
        trigger=IntervalTrigger(hours=6),
        args=[bot],
        id="reminders",
        max_instances=1,
        coalesce=True,
    )

    scheduler.start()
    logger.info("Scheduler started")

    try:
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown(wait=False)
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())