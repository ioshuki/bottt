from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    db_url: str = "sqlite+aiosqlite:///./bot.db"

    default_timezone: str = "Asia/Novosibirsk"
    default_language: str = "ru"
    default_daily_time: str = "10:00"
    default_mode: str = "normal"

    llm_enabled: bool = False
    llm_api_key: str = ""
    llm_base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/"
    llm_model: str = "gemini-2.5-flash-preview-04-17"

    app_env: str = "dev"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
