from sqlalchemy import Boolean, Enum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import StageEnum, TrackEnum


class Step(Base):
    __tablename__ = "steps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    step_code: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    track: Mapped[TrackEnum] = mapped_column(Enum(TrackEnum), nullable=False, index=True)
    stage: Mapped[StageEnum] = mapped_column(Enum(StageEnum), nullable=False)

    order_index: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)
    day_index: Mapped[int | None] = mapped_column(Integer, nullable=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    expected_user_action: Mapped[str] = mapped_column(Text, nullable=False)

    estimated_minutes: Mapped[int] = mapped_column(Integer, default=20, nullable=False)
    difficulty: Mapped[str] = mapped_column(String(50), default="normal", nullable=False)

    payload_json: Mapped[str | None] = mapped_column(Text, nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    progresses = relationship("UserStepProgress", back_populates="step")
