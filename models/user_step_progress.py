from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base
from models.enums import ProgressStatusEnum


class UserStepProgress(Base):
    __tablename__ = "user_step_progress"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    step_id: Mapped[int] = mapped_column(ForeignKey("steps.id"), nullable=False)
    status: Mapped[ProgressStatusEnum] = mapped_column(
        Enum(ProgressStatusEnum),
        default=ProgressStatusEnum.IN_PROGRESS,
        nullable=False,
    )
    user_response: Mapped[str | None] = mapped_column(Text, nullable=True)
    coach_feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    user = relationship("User", back_populates="progresses")
    step = relationship("Step", back_populates="progresses")
