from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from services.factory import build_services
from utils.keyboards import (
    main_menu_keyboard,
    settings_mode_keyboard,
    step_actions_keyboard,
)
from utils.labels import mode_label, timezone_label
from utils.motivations import get_praise_phrase
from utils.text import (
    help_text,
    next_step_intro_text,
    status_text,
    step_text,
    today_card_text,
    weak_input_text,
)
from utils.validators import looks_like_meaningful_step_response

router = Router()

DONE_PHRASES = {"готово", "готов", "сделал", "сделала", "done", "поехали", "выполнено"}


@router.message(F.text == "🚀 Мой шаг сегодня")
async def menu_today(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]
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
    help_message = await coach_service.generate_daily_task_help(user, profile, step)
    await message.answer(help_message, reply_markup=main_menu_keyboard())


@router.message(F.text == "✅ Выполнено")
async def menu_done(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("Активный шаг не найден.", reply_markup=main_menu_keyboard())
        return

    next_step = await step_service.mark_step_done(user, step)

    await message.answer(get_praise_phrase(), reply_markup=main_menu_keyboard())

    if next_step:
        await message.answer(next_step_intro_text(), reply_markup=main_menu_keyboard())
        await message.answer(
            step_text(next_step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )
    else:
        await message.answer("🎉 Похоже, ты прошёл все шаги.", reply_markup=main_menu_keyboard())


@router.message(F.text == "📊 Мой прогресс")
async def menu_status(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    done, total = await progress_repo.get_progress_counts(user.id)
    await message.answer(status_text(user, done, total), reply_markup=main_menu_keyboard())


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
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await settings_service.pause(user)
    await message.answer("⏸️ Пауза включена.", reply_markup=main_menu_keyboard())


@router.message(F.text == "▶️ Продолжить")
async def menu_resume(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await settings_service.resume(user)
    await message.answer("▶️ Продолжаем!", reply_markup=main_menu_keyboard())


@router.message(F.text == "⚙️ Настройки")
async def menu_settings(message: Message, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    await message.answer(
        "⚙️ Настройки\n\n"
        f"🌍 Часовой пояс: {timezone_label(str(user.timezone))}\n"
        f"🕒 Время плана: {user.daily_time}\n"
        f"⚙️ Режим: {mode_label(str(user.mode))}\n\n"
        "Выбери новый режим или измени время:",
        reply_markup=settings_mode_keyboard(),
    )


@router.message(F.text)
async def handle_text_message(message: Message, session: AsyncSession) -> None:
    if not message.text:
        return

    if message.text.startswith("/"):
        return

    lowered = message.text.lower().strip()

    # ── Обработка времени ─────────────────────────────────
    if lowered.startswith("время "):
        services = build_services(session)
        user_repo = services["user_repo"]
        settings_service = services["settings_service"]

        user = await user_repo.get_by_telegram_id(message.from_user.id)
        if not user:
            await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
            return

        new_time = lowered.replace("время ", "", 1).strip()
        parts = new_time.split(":")

        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            await message.answer("Неверный формат. Используй: время 09:30", reply_markup=main_menu_keyboard())
            return

        hours, minutes = int(parts[0]), int(parts[1])

        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            await message.answer("Время вне диапазона. От 00:00 до 23:59.", reply_markup=main_menu_keyboard())
            return

        normalized = f"{hours:02d}:{minutes:02d}"
        await settings_service.update_daily_time(user, normalized)
        await message.answer(f"🕒 Готово. Новое время: {normalized}", reply_markup=main_menu_keyboard())
        return

    # ── Обработка «Готово» и похожих фраз ────────────────
    if lowered in DONE_PHRASES:
        services = build_services(session)
        user_repo = services["user_repo"]
        step_service = services["step_service"]

        user = await user_repo.get_by_telegram_id(message.from_user.id)
        if not user:
            await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
            return

        step = await step_service.ensure_current_step(user)
        if not step:
            await message.answer("Активный шаг не найден.", reply_markup=main_menu_keyboard())
            return

        next_step = await step_service.mark_step_done(user, step)
        await message.answer(get_praise_phrase(), reply_markup=main_menu_keyboard())

        if next_step:
            await message.answer(next_step_intro_text(), reply_markup=main_menu_keyboard())
            await message.answer(
                step_text(next_step),
                parse_mode="HTML",
                reply_markup=step_actions_keyboard(),
            )
        else:
            await message.answer("🎉 Все шаги завершены. Ты молодец!", reply_markup=main_menu_keyboard())
        return

    # ── Проверка на слишком короткий ответ ───────────────
    if not looks_like_meaningful_step_response(message.text):
        await message.answer(weak_input_text(), reply_markup=main_menu_keyboard())
        return

    # ── Оценка ответа через AI ───────────────────────────
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]

    user = await user_repo.get_by_telegram_id(message.from_user.id)
    if not user:
        await message.answer("Сначала напиши /start", reply_markup=main_menu_keyboard())
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await message.answer("Сейчас нет активного шага.", reply_markup=main_menu_keyboard())
        return

    profile = await project_repo.get_by_user_id(user.id)
    evaluation = await coach_service.evaluate_user_response(
        user=user,
        profile=profile,
        step=step,
        user_response=message.text,
    )

    await message.answer(evaluation.feedback, reply_markup=main_menu_keyboard())

    if evaluation.accepted:
        next_step = await step_service.mark_step_done(
            user=user,
            step=step,
            user_response=message.text,
            coach_feedback=evaluation.feedback,
        )

        if next_step:
            await message.answer(next_step_intro_text(), reply_markup=main_menu_keyboard())
            await message.answer(
                step_text(next_step),
                parse_mode="HTML",
                reply_markup=step_actions_keyboard(),
            )
        else:
            await message.answer("🎉 Все шаги завершены.", reply_markup=main_menu_keyboard())
