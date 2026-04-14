from datetime import date, datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.daily_plan import DailyPlan


class DailyPlanRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_user_and_date(self, user_id: int, plan_date: date) -> DailyPlan | None:
        result = await self.session.execute(
            select(DailyPlan).where(
                DailyPlan.user_id == user_id,
                DailyPlan.date == plan_date,
            )
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        user_id: int,
        plan_date: date,
        summary: str,
        step_ids: str,
    ) -> DailyPlan:
        plan = DailyPlan(
            user_id=user_id,
            date=plan_date,
            summary=summary,
            step_ids=step_ids,
        )
        self.session.add(plan)
        await self.session.flush()
        return plan

    async def update(self, plan: DailyPlan, **kwargs) -> DailyPlan:
        for key, value in kwargs.items():
            setattr(plan, key, value)
        await self.session.flush()
        return plan

    async def mark_completed(self, plan: DailyPlan) -> DailyPlan:
        plan.completed = True
        await self.session.flush()
        return plan

    async def mark_sent(self, plan: DailyPlan) -> DailyPlan:
        plan.sent_at = datetime.utcnow()
        await self.session.flush()
        return plan

    async def find_today_plan(self, user_id: int, plan_date: date) -> DailyPlan | None:
        result = await self.session.execute(
            select(DailyPlan).where(
                DailyPlan.user_id == user_id,
                DailyPlan.date == plan_date,
            )
        )
        return result.scalar_one_or_none()
