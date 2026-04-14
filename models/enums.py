from enum import Enum


class StageEnum(str, Enum):
    SOCIAL_SETUP = "SOCIAL_SETUP"
    CHARACTER_LORE = "CHARACTER_LORE"
    APPEARANCE = "APPEARANCE"
    LOCATIONS = "LOCATIONS"
    PHOTO_PACK = "PHOTO_PACK"
    VIDEO_PACK = "VIDEO_PACK"
    LAUNCH = "LAUNCH"


class TrackEnum(str, Enum):
    MAIN = "main"
    INSTAGRAM_WARMUP = "instagram_warmup"
    TIKTOK_WARMUP = "tiktok_warmup"
    TELEGRAM_DAILY = "telegram_daily"
    INSTAGRAM_POSTING = "instagram_posting"
    TIKTOK_POSTING = "tiktok_posting"


class ModeEnum(str, Enum):
    EASY = "easy"
    NORMAL = "normal"
    SPRINT = "sprint"


class ProgressStatusEnum(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class DailyTaskStatusEnum(str, Enum):
    PENDING = "pending"
    DONE = "done"
    MISSED = "missed"


class LaunchStatusEnum(str, Enum):
    NOT_READY = "not_ready"
    IN_PROGRESS = "in_progress"
    READY = "ready"
