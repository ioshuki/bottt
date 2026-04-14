from models.step import Step
from models.user import User
from utils.labels import mode_label, stage_label, timezone_label


def start_text() -> str:
    return (
        "🤖 Добро пожаловать в AI Model Coach!\n\n"
        "Ты только что сделал первый шаг к тому,\n"
        "чтобы создать человека — которого не существует.\n\n"
        "Виртуальная AI модель. Твой персонаж.\n"
        "Твои правила. Твои деньги.\n\n"
        "Тысячи людей уже зарабатывают на AI-моделях\n"
        "в Instagram, TikTok и Telegram.\n"
        "Теперь твоя очередь. 🚀\n\n"
        "Я проведу тебя по каждому шагу —\n"
        "от идеи персонажа до первых денег.\n\n"
        "Готов начать? 👇"
    )


def help_text() -> str:
    return (
        "❓ Помощь\n\n"
        "Я помогаю тебе шаг за шагом собрать проект AI модели.\n\n"
        "Что можно делать прямо сейчас:\n"
        "• нажать «🚀 Мой шаг сегодня» — получить фокус дня\n"
        "• нажать «✅ Выполнено» — отметить шаг выполненным\n"
        "• отправить обычный текст — и я оценю ответ\n"
        "• открыть «⚙️ Настройки» — изменить режим и время\n\n"
        "Основные команды:\n"
        "/start — открыть бота и главное меню\n"
        "/today — показать план и текущий шаг\n"
        "/done — отметить текущий шаг выполненным\n"
        "/status — показать прогресс\n"
        "/pause — поставить работу на паузу\n"
        "/resume — продолжить\n"
        "/reset — начать шаги заново\n\n"
        "Если не хочется писать команды вручную — пользуйся кнопками внизу 👇"
    )


def step_text(step: Step) -> str:
    stage = stage_label(str(step.stage))

    return (
        "🧩 Текущий шаг\n\n"
        f"📍 Этап:\n{stage}\n\n"
        f"🎯 Задача:\n{step.title}\n\n"
        f"📝 Что сделать:\n{step.expected_user_action}\n\n"
        f"⏱ Время:\n~{step.estimated_minutes} мин.\n\n"
        f"📖 Контекст:\n{step.description}"
    )


def today_card_text(step: Step, plan_summary: str | None = None) -> str:
    header = "📅 План на сегодня\n\n"
    focus = f"🎯 Главный фокус:\n{step.title}\n\n"
    action = f"📝 Что сделать первым:\n{step.expected_user_action}\n\n"
    timing = f"⏱ Время:\n~{step.estimated_minutes} мин.\n\n"

    if plan_summary:
        summary = f"💡 План дня:\n{plan_summary}\n\n"
    else:
        summary = ""

    return header + focus + action + timing + summary


def status_text(user: User, done: int, total: int) -> str:
    current_stage = stage_label(str(user.current_stage)) if user.current_stage else "не выбран"
    current_step = str(user.current_step_id) if user.current_step_id else "нет"
    paused = "⏸️ Да" if user.is_paused else "▶️ Нет"
    mode = mode_label(str(user.mode))
    timezone = timezone_label(str(user.timezone))

    progress_line = f"{done}/{total}" if total > 0 else f"{done}"

    return (
        "📊 Статус проекта\n\n"
        f"📍 Текущий этап:\n{current_stage}\n\n"
        f"🧩 Текущий шаг ID:\n{current_step}\n\n"
        f"✅ Выполнено шагов:\n{progress_line}\n\n"
        f"🌍 Часовой пояс:\n{timezone}\n\n"
        f"🕒 Время ежедневного плана:\n{user.daily_time}\n\n"
        f"⚙️ Режим:\n{mode}\n\n"
        f"⏯ Пауза:\n{paused}"
    )


def weak_input_text() -> str:
    return (
        "Мне нужен чуть более содержательный ответ 👌\n\n"
        "Напиши 1–3 короткие, но конкретные мысли по текущему шагу.\n"
        "Например: варианты имени, описание стиля, список идей, 3 локации и т.д."
    )


def step_done_text() -> str:
    return "✅ Отлично, шаг отмечен как выполненный."


def next_step_intro_text() -> str:
    return "➡️ Переходим к следующему шагу:"
