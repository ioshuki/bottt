import re

TIME_RE = re.compile(r"^\d{2}:\d{2}$")


def is_valid_time(value: str) -> bool:
    if not TIME_RE.match(value):
        return False
    hours, minutes = value.split(":")
    return 0 <= int(hours) <= 23 and 0 <= int(minutes) <= 59


def looks_like_meaningful_step_response(text: str) -> bool:
    cleaned = text.strip().lower()

    if len(cleaned) < 8:
        return False

    weak_values = {
        "ок", "ok", "да", "yes", "ага",
        "понял", "норм", "хорошо", "+",
    }

    if cleaned in weak_values:
        return False

    return True
