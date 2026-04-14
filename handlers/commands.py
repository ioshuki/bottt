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
from utils.text import help_text, start_text, status_text, step_text, today_card_text

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
            "Прежде чем начать — подпишись на наш канал.\n"
            "Там выходят обновления, кейсы и полезные материалы\n"
            "по созданию AI моделей. 📢\n\n"
            "После подписки нажми кнопку ниже 👇",
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
        await message.answer(
            start_text(),
            reply_markup=main_menu_keyboard(),
        )
    else:
        await message.answer(
            "👋 Рад видеть тебя снова!\n\n"
            "Продолжаем работу над твоей AI моделью 💪\n"
            "Ты уже на пути — не останавливайся!",
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
    await message.answer(
        help_text(),
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("today"))
@router.message(Command("next"))
@router.message(Command("plan"))
async def cmd_today(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    coach_service = services["coach_service"]
    step_service = services["step_service"]
    planning_service = services["planning_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer(
            "Шагов пока нет.",
            reply_markup=main_menu_keyboard(),
        )
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
    help_message = await coach_service.generate_daily_task_help(user, profile, step)
    await message.answer(
        help_message,
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("done"))
async def cmd_done(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer(
            "Активный шаг не найден.",
            reply_markup=main_menu_keyboard(),
        )
        return

    next_step = await step_service.mark_step_done(user, step)

    await message.answer(
        "✅ Отлично, шаг отмечен как выполненный.",
        reply_markup=main_menu_keyboard(),
    )

    if next_step:
        await message.answer(
            "➡️ Следующий шаг:",
            reply_markup=main_menu_keyboard(),
        )
        await message.answer(
            step_text(next_step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )
    else:
        await message.answer(
            "🎉 Похоже, ты прошёл все шаги.",
            reply_markup=main_menu_keyboard(),
        )


@router.message(Command("status"))
async def cmd_status(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    done, total = await progress_repo.get_progress_counts(user.id)
    await message.answer(
        status_text(user, done, total),
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("pause"))
async def cmd_pause(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    await settings_service.pause(user)
    await message.answer(
        "⏸️ Пауза включена. Ежедневные планы временно остановлены.",
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("resume"))
async def cmd_resume(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    await settings_service.resume(user)
    await message.answer(
        "▶️ Отлично, продолжаем. Ежедневные планы снова активны.",
        reply_markup=main_menu_keyboard(),
    )


@router.message(Command("reset"))
async def cmd_reset(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(
            "Сначала напиши /start",
            reply_markup=main_menu_keyboard(),
        )
        return

    await step_service.reset_progress(user)
    await message.answer(
        "🔄 Прогресс по шагам сброшен. Настройки и профиль сохранены.",
        reply_markup=main_menu_keyboard(),
    )
