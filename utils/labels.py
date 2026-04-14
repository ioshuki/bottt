def stage_label(value: str) -> str:
    mapping = {
        "SOCIAL_SETUP": "📱 Подготовка и соцсети",
        "StageEnum.SOCIAL_SETUP": "📱 Подготовка и соцсети",
        "CHARACTER_LORE": "🧠 Создание персонажа",
        "StageEnum.CHARACTER_LORE": "🧠 Создание персонажа",
        "APPEARANCE": "🖼 Внешность модели",
        "StageEnum.APPEARANCE": "🖼 Внешность модели",
        "LOCATIONS": "📍 Локации",
        "StageEnum.LOCATIONS": "📍 Локации",
        "PHOTO_PACK": "📸 Фото-библиотека",
        "StageEnum.PHOTO_PACK": "📸 Фото-библиотека",
        "VIDEO_PACK": "🎬 Видео-пак",
        "StageEnum.VIDEO_PACK": "🎬 Видео-пак",
        "LAUNCH": "🚀 Запуск",
        "StageEnum.LAUNCH": "🚀 Запуск",
    }
    return mapping.get(str(value), str(value))


def mode_label(value: str) -> str:
    mapping = {
        "easy": "🐢 Лёгкий",
        "normal": "⚖️ Нормальный",
        "sprint": "🚀 Спринт",
        "ModeEnum.EASY": "🐢 Лёгкий",
        "ModeEnum.NORMAL": "⚖️ Нормальный",
        "ModeEnum.SPRINT": "🚀 Спринт",
    }
    return mapping.get(str(value), str(value))


def timezone_label(value: str) -> str:
    mapping = {
        "Europe/Moscow": "🕒 Москва (UTC+3)",
        "Europe/Kaliningrad": "🕒 Калининград (UTC+2)",
        "Europe/Samara": "🕒 Самара (UTC+4)",
        "Asia/Yekaterinburg": "🕒 Екатеринбург (UTC+5)",
        "Asia/Omsk": "🕒 Омск (UTC+6)",
        "Asia/Novosibirsk": "🕒 Новосибирск (UTC+7)",
        "Asia/Krasnoyarsk": "🕒 Красноярск (UTC+7)",
        "Asia/Irkutsk": "🕒 Иркутск (UTC+8)",
        "Asia/Yakutsk": "🕒 Якутск (UTC+9)",
        "Asia/Vladivostok": "🕒 Владивосток (UTC+10)",
        "Asia/Magadan": "🕒 Магадан (UTC+11)",
        "Asia/Kamchatka": "🕒 Камчатка (UTC+12)",
    }
    return mapping.get(str(value), str(value))
