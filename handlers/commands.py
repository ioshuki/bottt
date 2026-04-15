import json

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from config.settings import settings
from services.factory import build_services
from utils.keyboards import (
    main_menu_keyboard,
    step_actions_keyboard,
    subscription_keyboard,
)
from utils.text import (
    achievements_text,
    help_text,
    start_text,
    status_text,
    step_text,
    today_card_text,
)

router = Router()
CHANNEL = "@Ai_735Agency"


async def is_subscribed(bot, user_id: int, channel: str) -> bool:
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return member.status not in ("left", "kicked", "banned")
    except Exception:
        return False


@router.message(Command("start"))
async def cmd_start(message: Message, session: AsyncSession) -> None:
    bot = message.bot
    subscribed = await is_subscribed(bot, message.from_user.id, CHANNEL)

    if not subscribed:
        await message.answer(
            "👋 Привет!\n\n"
            "Подпишись на канал — там кейсы и обновления по AI-моделям 📢\n\n"
            "После подписки нажми кнопку 👇",
            reply_markup=subscription_keyboard(CHANNEL),
        )
        return

    services = build_services(session)
    onboarding_service = services["onboarding_service"]
    step_service = services["step_service"]

    user, created = await onboarding_service.get_or_create_user(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.full_name,
        language=settings.default_language,
        timezone=settings.default_timezone,
        daily_time=settings.default_daily_time,
        mode=settings.default_mode,
    )

    if created:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
    else:
        await message.answer(
            "👋 Снова в деле!\n\nПродолжаем — не останавливайся 💪",
            reply_markup=main_menu_keyboard(),
        )

    step = await step_service.ensure_current_step(user)
    if step:
        await message.answer(
            step_text(step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(help_text(), reply_markup=main_menu_keyboard())


@router.message(Command("today", "next", "plan"))
async def cmd_today(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    coach_service = services["coach_service"]
    step_service = services["step_service"]
    planning_service = services["planning_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("Шагов пока нет.", reply_markup=main_menu_keyboard())
        return

    await step_service.mark_step_in_progress(user, step)
    plan = await planning_service.get_or_create_daily_plan(user, step)

    await message.answer(
        today_card_text(step, plan.summary),
        reply_markup=main_menu_keyboard(),
    )
    await message.answer(
        step_text(step),
        parse_mode="HTML",
        reply_markup=step_actions_keyboard(),
    )

    profile = await project_repo.get_by_user_id(user.id)
    help_msg = await coach_service.generate_daily_task_help(user, profile, step)
    await message.answer(help_msg, reply_markup=main_menu_keyboard())


@router.message(Command("done"))
async def cmd_done(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("Активный шаг не найден.", reply_markup=main_menu_keyboard())
        return

    next_step = await step_service.mark_step_done(user, step)
    done, total = await progress_repo.get_progress_counts(user.id)

    # Достижение и секрет из payload
    achievement = None
    secret = None
    if step.payload_json:
        try:
            payload = json.loads(step.payload_json)
            achievement = payload.get("achievement")
            secret = payload.get("secret")
        except Exception:
            pass

    from utils.text import step_completed_text
    await message.answer(
        step_completed_text(done, total, achievement, secret),
        parse_mode="HTML",
        reply_markup=main_menu_keyboard(),
    )

    if next_step:
        await message.answer(
            step_text(next_step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )
    else:
        await message.answer(
            "🚀 ЛЕГЕНДА. Все уровни пройдены.\nAI-модель в эфире. Теперь только деньги.",
            reply_markup=main_menu_keyboard(),
        )


@router.message(Command("status"))
async def cmd_status(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    done, total = await progress_repo.get_progress_counts(user.id)
    await message.answer(status_text(user, done, total), reply_markup=main_menu_keyboard())


@router.message(Command("achievements"))
async def cmd_achievements(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]
    step_repo = services["step_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    done, total = await progress_repo.get_progress_counts(user.id)

    # Собираем бейджи из выполненных шагов
    badges = []
    completed = await progress_repo.get_completed_steps(user.id)
    for progress in completed:
        step = await step_repo.get_by_id(progress.step_id)
        if step and step.payload_json:
            try:
                payload = json.loads(step.payload_json)
                badge = payload.get("achievement")
                if badge:
                    badges.append(badge)
            except Exception:
                pass

    await message.answer(
        achievements_text(badges, done),
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("pause"))
async def cmd_pause(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await settings_service.pause(user)
    await message.answer("⏸️ Пауза. Напоминания остановлены.", reply_markup=main_menu_keyboard())


@router.message(Command("resume"))
async def cmd_resume(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await settings_service.resume(user)
    await message.answer("▶️ Продолжаем. Вперёд 🔥", reply_markup=main_menu_keyboard())


@router.message(Command("reset"))
async def cmd_reset(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await step_service.reset_progress(user)
    await message.answer(
        "🔄 Прогресс сброшен. Профиль сохранён.",
        reply_markup=main_menu_keyboard(),
    )
