import json
import logging

from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from services.factory import build_services
from utils.keyboards import main_menu_keyboard, step_actions_keyboard, settings_mode_keyboard
from utils.labels import mode_label, timezone_label
from utils.motivations import get_praise_phrase
from utils.text import (
    help_text,
    next_step_intro_text,
    start_text,
    status_text,
    step_text,
    step_completed_text,
    today_card_text,
    weak_input_text,
)
from utils.validators import looks_like_meaningful_step_response

logger = logging.getLogger(__name__)
router = Router()

DONE_PHRASES = {
    "готово", "готов", "сделал", "сделала", "done",
    "поехали", "выполнено", "готово!", "сделал!", "выполнил",
}

# Маппинг выборов в шаге 3
NATIONALITY_MAP = {
    "а": "Asian", "a": "Asian",
    "б": "Latin", "b": "Latin",
    "в": "European", "c": "European",
    "г": "American", "d": "American",
}
VIBE_MAP = {
    "а": "mysterious", "a": "mysterious",
    "б": "confident", "b": "confident",
    "в": "sporty", "c": "sporty",
    "г": "dark", "d": "dark",
}
AUDIENCE_MAP = {
    "а": "Men 18-35", "a": "Men 18-35",
    "б": "Women 18-28", "b": "Women 18-28",
    "в": "All", "c": "All",
}


def _parse_step3(text: str) -> dict | None:
    """Парсим ответ вида 'А, Б, А' или 'а б а' или 'а,б,а'"""
    cleaned = text.lower().replace(",", " ").replace(".", " ")
    parts = [p.strip() for p in cleaned.split() if p.strip()]
    if len(parts) < 3:
        return None
    nat = NATIONALITY_MAP.get(parts[0])
    vibe = VIBE_MAP.get(parts[1])
    audience = AUDIENCE_MAP.get(parts[2])
    if nat and vibe and audience:
        return {"nationality": nat, "vibe": vibe, "audience": audience}
    return None


async def _handle_step_done(
    message: Message,
    session,
    services: dict,
    user,
    step,
) -> None:
    """Общая логика завершения шага."""
    step_service = services["step_service"]
    progress_repo = services["progress_repo"]
    project_repo = services["project_repo"]

    # Парсим профиль на ключевых шагах
    if step.step_code == "lore_01_concept":
        parsed = _parse_step3(message.text)
        if parsed:
            profile = await project_repo.get_by_user_id(user.id)
            if not profile:
                profile = await project_repo.create(user.id)
            await project_repo.update(profile, **parsed)

    elif step.step_code == "lore_02_biography":
        # Сохраняем первое слово как имя модели если профиль пустой
        words = message.text.strip().split()
        if words:
            profile = await project_repo.get_by_user_id(user.id)
            if not profile:
                profile = await project_repo.create(user.id)
            if not profile.character_name:
                await project_repo.update(profile, character_name=words[0])

    elif step.step_code == "lore_03_pink_elephant":
        profile = await project_repo.get_by_user_id(user.id)
        if not profile:
            profile = await project_repo.create(user.id)
        await project_repo.update(profile, signature_trait=message.text.strip()[:255])

    next_step = await step_service.mark_step_done(user, step)
    done, total = await progress_repo.get_progress_counts(user.id)

    achievement = None
    secret = None
    if step.payload_json:
        try:
            payload = json.loads(step.payload_json)
            achievement = payload.get("achievement")
            secret = payload.get("secret")
        except Exception:
            pass

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


@router.message(F.text == "🚀 Мой шаг сегодня")
async def menu_today(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]
    planning_service = services["planning_service"]
    project_repo = services["project_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("✅ Все уровни пройдены! 🚀", reply_markup=main_menu_keyboard())
        return

    await step_service.mark_step_in_progress(user, step)
    plan = await planning_service.get_or_create_daily_plan(user, step)

    await message.answer(
        today_card_text(step, plan.summary if plan else None),
        reply_markup=main_menu_keyboard(),
    )
    await message.answer(
        step_text(step),
        parse_mode="HTML",
        reply_markup=step_actions_keyboard(),
    )

    profile = await project_repo.get_by_user_id(user.id)
    help_msg = await coach_service.generate_daily_task_help(user, profile, step)
    await message.answer(help_msg)


@router.message(F.text == "✅ Выполнено")
async def menu_done(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("Нет активного шага.", reply_markup=main_menu_keyboard())
        return

    await _handle_step_done(message, session, services, user, step)


@router.message(F.text == "📊 Мой прогресс")
async def menu_status(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
        return

    done, total = await progress_repo.get_progress_counts(user.id)
    await message.answer(status_text(user, done, total))


@router.message(F.text == "🧠 Помощь коуча")
async def menu_help(message: Message) -> None:
    await message.answer(help_text(), reply_markup=main_menu_keyboard())


@router.message(F.text == "⏸ Пауза")
async def menu_pause(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
        return

    await settings_service.pause(user)
    await message.answer("⏸ Пауза. Напоминания остановлены.", reply_markup=main_menu_keyboard())


@router.message(F.text == "▶️ Продолжить")
async def menu_resume(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer(start_text(), reply_markup=main_menu_keyboard())
        return

    await settings_service.resume(user)


@router.message(F.text == "⚙️ Настройки")
async def menu_settings(message: Message, session: AsyncSession) -> None:
    from utils.keyboards import settings_mode_keyboard
    services = build_services(session)
    user_repo = services["user_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await message.answer(
        f"⚙️ Настройки\n\n"
        f"🕒 Время плана: {user.daily_time}\n"
        f"🌍 Часовой пояс: {user.timezone}\n\n"
        f"Выбери что изменить:",
        reply_markup=settings_mode_keyboard(),
    )
