from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import ModeEnum, StageEnum


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str | None] = mapped_column(String(255), nullable=True)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    language: Mapped[str] = mapped_column(String(20), default="ru", nullable=False)
    timezone: Mapped[str] = mapped_column(String(100), default="Asia/Novosibirsk", nullable=False)
    daily_time: Mapped[str] = mapped_column(String(10), default="10:00", nullable=False)
    mode: Mapped[ModeEnum] = mapped_column(Enum(ModeEnum), default=ModeEnum.NORMAL, nullable=False)

    current_stage: Mapped[StageEnum | None] = mapped_column(Enum(StageEnum), nullable=True)
    current_step_id: Mapped[int | None] = mapped_column(Integer, nullable=True)

    is_paused: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    onboarding_completed: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    progresses = relationship("UserStepProgress", back_populates="user")
    project_profile = relationship("ProjectProfile", back_populates="user", uselist=False)
    daily_plans = relationship("DailyPlan", back_populates="user")
