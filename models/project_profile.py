from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class ProjectProfile(Base):
    __tablename__ = "project_profiles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, unique=True)

    project_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    goal: Mapped[str | None] = mapped_column(Text, nullable=True)
    style: Mapped[str | None] = mapped_column(String(255), nullable=True)
    platforms: Mapped[str | None] = mapped_column(String(255), nullable=True)

    character_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    lore_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    appearance_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    location_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    launch_status: Mapped[str | None] = mapped_column(String(50), nullable=True)

    user = relationship("User", back_populates="project_profile")
