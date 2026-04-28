from models.step import Step
from models.user import User
from utils.labels import mode_label, stage_label, timezone_label


# ── Прогресс-бар ──────────────────────────────────────────────────────────

TOTAL_STEPS = 26  # 10 основных + 7 Instagram + 7 TikTok + 2 запуска

TITLES = [
    (0,  "😶 НИКТО (пока)"),
    (1,  "🔧 СТРОИТЕЛЬ"),
    (3,  "🏭 СОЗДАТЕЛЬ"),
    (5,  "⚡ АРХИТЕКТОР"),
    (7,  "🔥 ПРОДЮСЕР"),
    (9,  "💎 ЭЛИТА"),
    (16, "🏹 ОХОТНИК"),
    (23, "👑 БОСС"),
    (26, "🚀 ЛЕГЕНДА"),
]

TITLE_UNLOCKS = {
    1:  "🔧 СТРОИТЕЛЬ",
    3:  "🏭 СОЗДАТЕЛЬ",
    5:  "⚡ АРХИТЕКТОР",
    7:  "🔥 ПРОДЮСЕР",
    9:  "💎 ЭЛИТА",
    16: "🏹 ОХОТНИК",
    23: "👑 БОСС",
    26: "🚀 ЛЕГЕНДА",
}


def progress_bar(done: int, total: int = TOTAL_STEPS) -> str:
    filled = round((done / total) * 10) if total > 0 else 0
    bar = "▓" * filled + "░" * (10 - filled)
    percent = round((done / total) * 100) if total > 0 else 0
    return f"{bar} {percent}%"


def title_for_progress(done: int) -> str:
    title = TITLES[0][1]
    for threshold, label in TITLES:
        if done >= threshold:
            title = label
    return title


def get_title_unlock_message(done: int) -> str | None:
    if done in TITLE_UNLOCKS:
        return f"🆕 Новый титул: {TITLE_UNLOCKS[done]}\nДо этого дошли единицы."
    return None


def step_completed_text(
    done: int,
    total: int,
    achievement: str | None = None,
    secret: str | None = None,
) -> str:
    bar = progress_bar(done, total)
    title = title_for_progress(done)
    title_msg = get_title_unlock_message(done)

    lines = ["⚡ ЗАКРЫТО\n"]

    if achievement:
        lines.append(f"{achievement}\n")

    if title_msg:
        lines.append(f"{title_msg}\n")

    lines.append(f"{bar} • {title}")

    if secret:
        lines.append(f"\n🔓 {secret}")

    return "\n".join(lines)


# ── Стандартные тексты ────────────────────────────────────────────────────

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
        "Готов начать? Нажми кнопку ниже 👇"
    )


def help_text() -> str:
    return (
        "❓ Помощь\n\n"
        "/today — текущий шаг\n"
        "/done — отметить шаг выполненным\n"
        "/status — прогресс\n"
        "/achievements — твои достижения\n"
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
        f"📅 {step.title}\n"
        f"⏱ ~{step.estimated_minutes} мин.\n\n"
        f"{step.description}"
    )
    if plan_summary:
        text += f"\n\n💡 {plan_summary}"
    return text


def status_text(user: User, done: int, total: int) -> str:
    current_stage = stage_label(str(user.current_stage)) if user.current_stage else "не выбран"
    paused = "⏸️ На паузе" if user.is_paused else "▶️ Активен"
    mode = mode_label(str(user.mode))
    timezone = timezone_label(str(user.timezone))
    bar = progress_bar(done, TOTAL_STEPS)
    title = title_for_progress(done)
    return (
        f"📊 Прогресс\n\n"
        f"{bar} • {title}\n\n"
        f"📍 Этап: {current_stage}\n"
        f"✅ Выполнено: {done}/{total}\n"
        f"🌍 Часовой пояс: {timezone}\n"
        f"🕒 Время плана: {user.daily_time}\n"
        f"⚙️ Режим: {mode}\n"
        f"⏯ Статус: {paused}"
    )


def achievements_text(badges: list[str], done: int) -> str:
    title = title_for_progress(done)
    bar = progress_bar(done, TOTAL_STEPS)
    if not badges:
        return (
            f"👑 ДОСТИЖЕНИЯ\n\n"
            f"Пока пусто. Начни первый шаг 👇\n\n"
            f"{bar} • {title}"
        )
    badges_text = "\n".join(badges)
    return (
        f"👑 ТВОИ ДОСТИЖЕНИЯ\n\n"
        f"{badges_text}\n\n"
        f"Разблокировано: {len(badges)} из 12\n"
        f"{bar} • {title}"
    )


def weak_input_text() -> str:
    return (
        "Напиши чуть подробнее 👌\n\n"
        "1–3 детали по текущему шагу."
    )


def step_done_text() -> str:
    return "✅ Шаг выполнен! Отличная работа 💪"


def next_step_intro_text() -> str:
    return "➡️ Следующий шаг:"