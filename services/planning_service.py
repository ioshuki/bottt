from datetime import datetime
from zoneinfo import ZoneInfo

from models.step import Step
from models.user import User
from repositories.daily_plan_repository import DailyPlanRepository
from repositories.step_repository import StepRepository


class PlanningService:
    def __init__(
        self,
        daily_plan_repo: DailyPlanRepository,
        step_repo: StepRepository,
    ) -> None:
        self.daily_plan_repo = daily_plan_repo
        self.step_repo = step_repo

    async def get_plan_steps(self, user: User, current_step: Step | None) -> list[Step]:
        if not current_step:
            return []

        steps = [current_step]

        mode_value = str(user.mode).lower()

        if "sprint" in mode_value:
            next_step = await self.step_repo.get_next_step(current_step)
            if next_step:
                steps.append(next_step)

        return steps

    async def build_summary(self, user: User, steps: list[Step]) -> str:
        if not steps:
            return "Сегодня активных задач пока нет."

        if len(steps) == 1:
            return f"Сегодня твой главный фокус: {steps[0].title}"

        joined_titles = "\n".join([f"• {step.title}" for step in steps])
        return (
            "Сегодня у тебя короткий спринт.\n\n"
            "Фокус дня:\n"
            f"{joined_titles}"
        )

    async def get_or_create_daily_plan(
        self,
        user: User,
        current_step: Step | None,
    ):
        user_now = datetime.now(ZoneInfo(user.timezone))
        today = user_now.date()

        existing = await self.daily_plan_repo.get_by_user_and_date(user.id, today)
        if existing:
            return existing

        steps = await self.get_plan_steps(user, current_step)
        summary = await self.build_summary(user, steps)
        step_ids = ",".join(str(step.id) for step in steps)

        return await self.daily_plan_repo.create(
            user_id=user.id,
            plan_date=today,
            summary=summary,
            step_ids=step_ids,
        )
