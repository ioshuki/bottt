"""
Подстановка значений из профиля пользователя в текст шага.

Поддерживает:
- именованные плейсхолдеры: {character_name}, {nationality}, {vibe}, {audience}, {signature_trait}
- человекочитаемые подсказки вида "[из шага 3]" — заменяются по смыслу строки
"""

from __future__ import annotations

from models.project_profile import ProjectProfile
from models.step import Step


# Человеко-читаемые названия национальностей и вайбов для подстановки в текст
NATIONALITY_LABELS = {
    "Asian": "Азия",
    "Latin": "Латинка",
    "European": "Европа",
    "American": "США",
}

VIBE_LABELS = {
    "mysterious": "Загадочная",
    "confident": "Дерзкая",
    "sporty": "Спортивная",
    "dark": "Мистическая",
}

AUDIENCE_LABELS = {
    "Men 18-35": "Мужчины 18–35",
    "Women 18-28": "Женщины 18–28",
    "All": "Все",
}


def _profile_value(profile: ProjectProfile | None, key: str) -> str | None:
    """Достаём значение из профиля и переводим в человеко-читаемый вид."""
    if not profile:
        return None

    raw = getattr(profile, key, None)
    if not raw:
        return None

    if key == "nationality":
        return NATIONALITY_LABELS.get(raw, raw)
    if key == "vibe":
        return VIBE_LABELS.get(raw, raw)
    if key == "audience":
        return AUDIENCE_LABELS.get(raw, raw)

    return str(raw)


def _render_named_placeholders(text: str, profile: ProjectProfile | None) -> str:
    """Заменяет {character_name}, {nationality}, {vibe}, {audience}, {signature_trait}."""
    keys = ["character_name", "nationality", "vibe", "audience", "signature_trait"]
    for key in keys:
        placeholder = "{" + key + "}"
        if placeholder in text:
            value = _profile_value(profile, key) or "—"
            text = text.replace(placeholder, value)
    return text


def _render_step3_hints(text: str, profile: ProjectProfile | None) -> str:
    """
    Заменяет подсказки "[из шага 3]" на реальные значения,
    исходя из контекста строки (Национальность / Вайб / Аудитория).
    """
    if "[из шага 3]" not in text:
        return text

    lines = text.split("\n")
    result = []
    for line in lines:
        if "[из шага 3]" in line:
            lower = line.lower()
            if "национальн" in lower:
                value = _profile_value(profile, "nationality") or "[из шага 3]"
                line = line.replace("[из шага 3]", value)
            elif "вайб" in lower or "стиль" in lower:
                value = _profile_value(profile, "vibe") or "[из шага 3]"
                line = line.replace("[из шага 3]", value)
            elif "аудитор" in lower or "для кого" in lower:
                value = _profile_value(profile, "audience") or "[из шага 3]"
                line = line.replace("[из шага 3]", value)
        result.append(line)
    return "\n".join(result)


def render_text(text: str | None, profile: ProjectProfile | None) -> str:
    """
    Главная функция — прогоняет текст через все правила подстановки.
    """
    if not text:
        return ""

    text = _render_named_placeholders(text, profile)
    text = _render_step3_hints(text, profile)
    return text


def render_step(step: Step, profile: ProjectProfile | None) -> Step:
    """
    Возвращает копию шага с подставленными значениями в title/description/expected_user_action.
    Не сохраняет в БД — только меняет объект в памяти для отображения.
    """
    step.title = render_text(step.title, profile)
    step.description = render_text(step.description, profile)
    step.expected_user_action = render_text(step.expected_user_action, profile)
    return step