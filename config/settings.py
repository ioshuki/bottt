from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bot_token: str
    db_url: str = "sqlite+aiosqlite:///./bot.db"

    subscription_channel: str = "@Ai_735Agency"

    default_timezone: str = "Asia/Novosibirsk"
    default_language: str = "ru"
    default_daily_time: str = "10:00"
    default_mode: str = "normal"

    llm_enabled: bool = False
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"

    app_env: str = "dev"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()