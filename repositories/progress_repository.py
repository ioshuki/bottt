from datetime import date

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_step_progress import UserStepProgress
from models.enums import ProgressStatusEnum


class ProgressRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_user_and_step(
        self, user_id: int, step_id: int
    ) -> UserStepProgress | None:
        result = await self.session.execute(
            select(UserStepProgress).where(
                UserStepProgress.user_id == user_id,
                UserStepProgress.step_id == step_id,
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        user_id: int,
        step_id: int,
        status: ProgressStatusEnum = ProgressStatusEnum.IN_PROGRESS,
        user_response: str | None = None,
        coach_feedback: str | None = None,
    ) -> UserStepProgress:
        progress = UserStepProgress(
            user_id=user_id,
            step_id=step_id,
            status=status,
            user_response=user_response,
            coach_feedback=coach_feedback,
        )
        self.session.add(progress)
        await self.session.flush()
        return progress

    async def update(self, progress: UserStepProgress, **kwargs) -> UserStepProgress:
        for key, value in kwargs.items():
            setattr(progress, key, value)
        await self.session.flush()
        return progress

    async def get_progress_counts(self, user_id: int) -> tuple[int, int]:
        total_result = await self.session.execute(
            select(func.count(UserStepProgress.id)).where(
                UserStepProgress.user_id == user_id
            )
        )
        done_result = await self.session.execute(
            select(func.count(UserStepProgress.id)).where(
                UserStepProgress.user_id == user_id,
                UserStepProgress.status == ProgressStatusEnum.DONE,
            )
        )
        total = total_result.scalar_one() or 0
        done = done_result.scalar_one() or 0
        return done, total

    async def get_last_done_date(self, user_id: int) -> date | None:
        result = await self.session.execute(
            select(UserStepProgress.updated_at).where(
                UserStepProgress.user_id == user_id,
                UserStepProgress.status == ProgressStatusEnum.DONE,
            ).order_by(UserStepProgress.updated_at.desc()).limit(1)
        )
        row = result.scalar_one_or_none()
        if row is None:
            return None
        return row.date() if hasattr(row, "date") else None
    async def get_completed_steps(self, user_id: int) -> list:
        result = await self.session.execute(
            select(UserStepProgress).where(
                UserStepProgress.user_id == user_id,
                UserStepProgress.status == ProgressStatusEnum.DONE,
            ).order_by(UserStepProgress.updated_at.asc())
        )
        return list(result.scalars().all())
