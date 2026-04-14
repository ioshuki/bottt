from datetime import datetime
from zoneinfo import ZoneInfo

from aiogram import Bot

from db.session import SessionLocal
from services.factory import build_services
from utils.keyboards import main_menu_keyboard, step_actions_keyboard
from utils.text import step_text, today_card_text


async def send_daily_plans(bot: Bot) -> None:
    async with SessionLocal() as session:
        services = build_services(session)

        user_repo = services["user_repo"]
        project_repo = services["project_repo"]
        step_service = services["step_service"]
        planning_service = services["planning_service"]
        daily_plan_repo = services["daily_plan_repo"]
        coach_service = services["coach_service"]

        users = await user_repo.list_active_users()

        for user in users:
            try:
                if user.is_paused:
                    continue

                user_now = datetime.now(ZoneInfo(user.timezone))
                today = user_now.date()
                current_time = user_now.strftime("%H:%M")

                if current_time != user.daily_time:
                    continue

                existing_plan = await daily_plan_repo.get_by_user_and_date(user.id, today)
                if existing_plan and existing_plan.sent_at is not None:
                    continue

                step = await step_service.ensure_current_step(user)
                if not step:
                    continue

                await step_service.mark_step_in_progress(user, step)
                plan = await planning_service.get_or_create_daily_plan(user, step)

                await bot.send_message(
                    chat_id=user.telegram_id,
                    text=today_card_text(step, plan.summary),
                    reply_markup=main_menu_keyboard(),
                )

                await bot.send_message(
                    chat_id=user.telegram_id,
                    text=step_text(step),
                    reply_markup=step_actions_keyboard(),
                )

                profile = await project_repo.get_by_user_id(user.id)
                help_message = await coach_service.generate_daily_task_help(user, profile, step)

                await bot.send_message(
                    chat_id=user.telegram_id,
                    text=help_message,
                    reply_markup=main_menu_keyboard(),
                )

                await daily_plan_repo.mark_sent(plan)
                await session.commit()

            except Exception as e:
                print(f"[scheduler] error for user {user.telegram_id}: {e}")
                await session.rollback()
                continue
