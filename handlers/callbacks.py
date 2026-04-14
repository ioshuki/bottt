from aiogram import Router, F
from aiogram.types import CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from services.factory import build_services
from utils.keyboards import main_menu_keyboard, step_actions_keyboard, subscription_keyboard
from utils.motivations import get_praise_phrase
from utils.text import next_step_intro_text, start_text, step_text
from utils.labels import mode_label, timezone_label

CHANNEL = "@Ai_735Agency"

router = Router()


@router.callback_query(F.data == "check_subscription")
async def cb_check_subscription(callback: CallbackQuery, session: AsyncSession) -> None:
    from aiogram.exceptions import TelegramBadRequest
    from aiogram import Bot

    bot: Bot = callback.bot
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL, user_id=callback.from_user.id)
        is_subscribed = member.status not in ("left", "kicked")
    except TelegramBadRequest:
        is_subscribed = False

    if not is_subscribed:
        await callback.answer("Ты ещё не подписался на канал 😊", show_alert=True)
        return

    services = build_services(session)
    user_repo = services["user_repo"]
    onboarding_service = services["onboarding_service"]
    step_service = services["step_service"]

    user, _ = await onboarding_service.get_or_create_user(
        telegram_id=callback.from_user.id,
        username=callback.from_user.username,
        name=callback.from_user.full_name,
    )

    await callback.message.answer(start_text(), reply_markup=main_menu_keyboard())

    step = await step_service.ensure_current_step(user)
    if step:
        await callback.message.answer(
            step_text(step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )

    await callback.answer()


@router.callback_query(F.data == "step_done")
async def cb_step_done(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    step_service = services["step_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await callback.message.answer("Активный шаг не найден.")
        await callback.answer()
        return

    next_step = await step_service.mark_step_done(user, step)

    await callback.message.answer(get_praise_phrase())

    if next_step:
        await callback.message.answer(next_step_intro_text())
        await callback.message.answer(
            step_text(next_step),
            parse_mode="HTML",
            reply_markup=step_actions_keyboard(),
        )
    else:
        await callback.message.answer(
            "🎉 Ты прошёл все шаги! AI-модель создана. Легенда 🏆",
            reply_markup=main_menu_keyboard(),
        )

    await callback.answer()


@router.callback_query(F.data == "step_status")
async def cb_step_status(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    progress_repo = services["progress_repo"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    done, total = await progress_repo.get_progress_counts(user.id)

    await callback.message.answer(
        f"📊 Мини-статус\n\n"
        f"📍 Этап: {user.current_stage}\n"
        f"✅ Выполнено: {done}/{total} шагов"
    )
    await callback.answer()


@router.callback_query(F.data == "step_example")
async def cb_step_example(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await callback.message.answer("Активный шаг не найден.")
        await callback.answer()
        return

    await callback.answer("Генерирую пример... ⏳")

    profile = await project_repo.get_by_user_id(user.id)
    example = await coach_service.generate_example(user, profile, step)

    await callback.message.answer(example)


@router.callback_query(F.data == "step_simplify")
async def cb_step_simplify(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await callback.message.answer("Активный шаг не найден.")
        await callback.answer()
        return

    await callback.answer("Упрощаю задачу... ⏳")

    profile = await project_repo.get_by_user_id(user.id)
    simplified = await coach_service.simplify_step(user, profile, step)

    await callback.message.answer(simplified)


@router.callback_query(F.data == "step_references")
async def cb_step_references(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    project_repo = services["project_repo"]
    step_service = services["step_service"]
    coach_service = services["coach_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    step = await step_service.ensure_current_step(user)
    if not step:
        await callback.message.answer("Активный шаг не найден.")
        await callback.answer()
        return

    await callback.answer("Подбираю референсы под твою модель... ⏳")

    profile = await project_repo.get_by_user_id(user.id)
    references = await coach_service.generate_references(user, profile, step)

    await callback.message.answer(
        f"💡 Референсы для твоей AI-модели:\n\n{references}"
    )


@router.callback_query(F.data == "settings_time")
async def cb_settings_time(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "Чтобы изменить время ежедневного плана, отправь сообщение в формате:\n\n"
        "время 09:30\n\n"
        "Пример:\n"
        "время 21:15"
    )
    await callback.answer()


@router.callback_query(F.data.startswith("set_mode:"))
async def cb_set_mode(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    mode = callback.data.split(":", 1)[1]
    await settings_service.update_mode(user, mode)

    await callback.message.answer(f"⚙️ Готово. Новый режим: {mode_label(mode)}")
    await callback.answer("Режим обновлён ✅")


@router.callback_query(F.data.startswith("set_timezone:"))
async def cb_set_timezone(callback: CallbackQuery, session: AsyncSession) -> None:
    services = build_services(session)
    user_repo = services["user_repo"]
    settings_service = services["settings_service"]

    user = await user_repo.get_by_telegram_id(callback.from_user.id)
    if not user:
        await callback.message.answer("Сначала напиши /start")
        await callback.answer()
        return

    timezone_value = callback.data.split(":", 1)[1]
    await settings_service.update_timezone(user, timezone_value)

    await callback.message.answer(
        f"🌍 Готово. Часовой пояс: {timezone_label(timezone_value)}"
    )
    await callback.answer("Часовой пояс обновлён ✅")
