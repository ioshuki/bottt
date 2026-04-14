def stage_label(value: str) -> str:
    mapping = {
        "SOCIAL_SETUP": "Соцсети и база проекта",
        "StageEnum.SOCIAL_SETUP": "Соцсети и база проекта",

        "CHARACTER_LORE": "Лор персонажа",
        "StageEnum.CHARACTER_LORE": "Лор персонажа",

        "APPEARANCE": "Внешность",
        "StageEnum.APPEARANCE": "Внешность",

        "LOCATIONS": "Локации",
        "StageEnum.LOCATIONS": "Локации",

        "PHOTO_PACK": "Фотопак",
        "StageEnum.PHOTO_PACK": "Фотопак",

        "VIDEO_PACK": "Видеопак",
        "StageEnum.VIDEO_PACK": "Видеопак",

        "LAUNCH": "Запуск",
        "StageEnum.LAUNCH": "Запуск",
    }
    return mapping.get(str(value), str(value))


def mode_label(value: str) -> str:
    mapping = {
        "easy": "Лёгкий",
        "normal": "Нормальный",
        "sprint": "Спринт",

        "ModeEnum.EASY": "Лёгкий",
        "ModeEnum.NORMAL": "Нормальный",
        "ModeEnum.SPRINT": "Спринт",
    }
    return mapping.get(str(value), str(value))


def timezone_label(value: str) -> str:
    mapping = {
        "Asia/Novosibirsk": "Новосибирск",
        "Europe/Moscow": "Москва",
    }
    return mapping.get(str(value), str(value))
