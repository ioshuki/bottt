from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def step_actions_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Готово", callback_data="step_done"),
                InlineKeyboardButton(text="📍 Статус", callback_data="step_status"),
            ],
            [
                InlineKeyboardButton(text="📌 Пример", callback_data="step_example"),
                InlineKeyboardButton(text="🔍 Объясни проще", callback_data="step_simplify"),
            ],
            [
                InlineKeyboardButton(text="💡 Референсы для моей модели", callback_data="step_references"),
            ],
        ]
    )


def settings_mode_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🐢 Easy", callback_data="set_mode:easy"),
                InlineKeyboardButton(text="⚖️ Normal", callback_data="set_mode:normal"),
                InlineKeyboardButton(text="🚀 Sprint", callback_data="set_mode:sprint"),
            ],
            [InlineKeyboardButton(text="🕒 Изменить время", callback_data="settings_time")],
            [
                InlineKeyboardButton(
                    text="🌍 Часовой пояс: Новосибирск",
                    callback_data="set_timezone:Asia/Novosibirsk",
                )
            ],
        ]
    )


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🚀 Мой шаг сегодня"),
                KeyboardButton(text="✅ Выполнено"),
            ],
            [
                KeyboardButton(text="📊 Мой прогресс"),
                KeyboardButton(text="🧠 Помощь коуча"),
            ],
            [
                KeyboardButton(text="⏸ Пауза"),
                KeyboardButton(text="▶️ Продолжить"),
            ],
            [
                KeyboardButton(text="⚙️ Настройки"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выбери действие…",
    )


def subscription_keyboard(channel: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Подписаться на канал",
                    url=f"https://t.me/{channel.lstrip('@')}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Я подписался",
                    callback_data="check_subscription",
                )
            ],
        ]
    )
