def merge_summary(existing: str | None, new_text: str, max_chars: int = 1200) -> str:
    """
    Простой MVP-merge для memory summary:
    - добавляет новый блок
    - убирает пустые строки
    - ограничивает общий размер
    - сохраняет последние наиболее релевантные части
    """
    parts = []

    if existing:
        parts.extend([p.strip() for p in existing.split("\n") if p.strip()])

    parts.extend([p.strip() for p in new_text.split("\n") if p.strip()])

    merged = []
    seen = set()

    for part in parts:
        key = part.lower()
        if key not in seen:
            seen.add(key)
            merged.append(part)

    result = "\n".join(merged).strip()

    if len(result) <= max_chars:
        return result

    trimmed_parts = []
    current_len = 0

    for part in reversed(merged):
        needed = len(part) + (1 if trimmed_parts else 0)
        if current_len + needed > max_chars:
            break
        trimmed_parts.append(part)
        current_len += needed

    return "\n".join(reversed(trimmed_parts)).strip()
