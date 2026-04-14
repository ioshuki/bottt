from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from models.step import Step


class StepRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_id(self, step_id: int) -> Step | None:
        result = await self.session.execute(
            select(Step).where(Step.id == step_id)
        )
        return result.scalar_one_or_none()

    async def get_first_active(self) -> Step | None:
        result = await self.session.execute(
            select(Step)
            .where(Step.is_active.is_(True))
            .order_by(Step.order_index.asc())
        )
        return result.scalars().first()

    async def get_next_step(self, current_step: Step) -> Step | None:
        result = await self.session.execute(
            select(Step)
            .where(
                and_(
                    Step.is_active.is_(True),
                    Step.order_index > current_step.order_index,
                )
            )
            .order_by(Step.order_index.asc())
        )
        return result.scalars().first()

    async def list_by_stage(self, stage: str) -> list[Step]:
        result = await self.session.execute(
            select(Step)
            .where(Step.stage == stage)
            .order_by(Step.order_index.asc())
        )
        return list(result.scalars().all())
