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
        "Готов начать? Нажми кнопку ниже 👇"
    )


def help_text() -> str:
    return (
        "❓ Помощь\n\n"
        "Я помогаю тебе шаг за шагом создать AI-модель.\n\n"
        "Что делать:\n"
        "• «🚀 Мой шаг сегодня» — получить задачу дня\n"
        "• «✅ Выполнено» — отметить шаг готовым\n"
        "• Напиши «Готово» — тоже отметит шаг\n"
        "• «⚙️ Настройки» — изменить режим и время\n\n"
        "Команды:\n"
        "/start — главное меню\n"
        "/today — текущий шаг\n"
        "/done — отметить шаг выполненным\n"
        "/status — прогресс\n"
        "/pause — пауза\n"
        "/resume — продолжить\n"
        "/reset — начать заново\n\n"
        "Пользуйся кнопками — так проще 👇"
    )


def step_text(step: Step) -> str:
    return (
        f"🎯 {step.title}\n\n"
        f"{step.expected_user_action}\n\n"
        f"⏱ ~{step.estimated_minutes} мин."
    )


def today_card_text(step: Step, plan_summary: str | None = None) -> str:
    text = (
        "📅 Твой шаг на сегодня:\n\n"
        f"🎯 {step.title}\n"
        f"⏱ ~{step.estimated_minutes} мин.\n\n"
        f"📖 {step.description}"
    )
    if plan_summary:
        text += f"\n\n💡 {plan_summary}"
    return text


def status_text(user: User, done: int, total: int) -> str:
    current_stage = stage_label(str(user.current_stage)) if user.current_stage else "не выбран"
    paused = "⏸️ На паузе" if user.is_paused else "▶️ Активен"
    mode = mode_label(str(user.mode))
    timezone = timezone_label(str(user.timezone))
    progress_line = f"{done}/{total}" if total > 0 else f"{done}"

    return (
        "📊 Твой прогресс\n\n"
        f"📍 Этап: {current_stage}\n"
        f"✅ Выполнено: {progress_line} шагов\n"
        f"🌍 Часовой пояс: {timezone}\n"
        f"🕒 Время плана: {user.daily_time}\n"
        f"⚙️ Режим: {mode}\n"
        f"⏯ Статус: {paused}"
    )


def weak_input_text() -> str:
    return (
        "Напиши чуть подробнее 👌\n\n"
        "Например: имя модели, стиль, идея — "
        "любые 1–3 конкретные детали по текущему шагу."
    )


def step_done_text() -> str:
    return "✅ Шаг выполнен! Отличная работа 💪"


def next_step_intro_text() -> str:
    return "➡️ Следующий шаг:"
