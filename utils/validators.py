import re


TIME_RE = re.compile(r"^\d{2}:\d{2}$")


def is_valid_time(value: str) -> bool:
    if not TIME_RE.match(value):
        return False

    hours, minutes = value.split(":")
    h = int(hours)
    m = int(minutes)
    return 0 <= h <= 23 and 0 <= m <= 59


def looks_like_meaningful_step_response(text: str) -> bool:
    cleaned = text.strip().lower()

    if len(cleaned) < 8:
        return False

    weak_values = {
        "ок",
        "ok",
        "да",
        "yes",
        "ага",
        "понял",
        "готово",
        "норм",
        "хорошо",
        "+",
        "done",
    }

    if cleaned in weak_values:
        return False

    return True
