from datetime import datetime
from zoneinfo import ZoneInfo

from models.enums import ProgressStatusEnum
from models.step import Step
from models.user import User
from repositories.daily_plan_repository import DailyPlanRepository
from repositories.progress_repository import ProgressRepository
from repositories.step_repository import StepRepository
from repositories.user_repository import UserRepository


class StepService:
    def __init__(
        self,
        step_repo: StepRepository,
        progress_repo: ProgressRepository,
        user_repo: UserRepository,
        daily_plan_repo: DailyPlanRepository,
    ) -> None:
        self.step_repo = step_repo
        self.progress_repo = progress_repo
        self.user_repo = user_repo
        self.daily_plan_repo = daily_plan_repo

    async def ensure_current_step(self, user: User) -> Step | None:
        if user.current_step_id:
            step = await self.step_repo.get_by_id(user.current_step_id)
            if step:
                return step

        first_step = await self.step_repo.get_first_active()
        if not first_step:
            return None

        await self.user_repo.update(
            user,
            current_step_id=first_step.id,
            current_stage=first_step.stage,
        )
        return first_step

    async def mark_step_done(
        self,
        user: User,
        step: Step,
        user_response: str | None = None,
        coach_feedback: str | None = None,
    ) -> Step | None:
        progress = await self.progress_repo.get_by_user_and_step(user.id, step.id)
        if progress:
            await self.progress_repo.update(
                progress,
                status=ProgressStatusEnum.DONE,
                user_response=user_response,
                coach_feedback=coach_feedback,
            )
        else:
            await self.progress_repo.create(
                user_id=user.id,
                step_id=step.id,
                status=ProgressStatusEnum.DONE,
                user_response=user_response,
                coach_feedback=coach_feedback,
            )

        try:
            user_now = datetime.now(ZoneInfo(user.timezone))
            today_plan = await self.daily_plan_repo.find_today_plan(user.id, user_now.date())
            if today_plan and not today_plan.completed:
                step_ids = [item.strip() for item in (today_plan.step_ids or "").split(",") if item.strip()]
                if str(step.id) in step_ids:
                    await self.daily_plan_repo.mark_completed(today_plan)
        except Exception:
            pass

        next_step = await self.step_repo.get_next_step(step)
        if next_step:
            await self.user_repo.update(
                user,
                current_step_id=next_step.id,
                current_stage=next_step.stage,
            )
            return next_step

        return None

    async def mark_step_in_progress(self, user: User, step: Step) -> None:
        progress = await self.progress_repo.get_by_user_and_step(user.id, step.id)
        if not progress:
            await self.progress_repo.create(
                user_id=user.id,
                step_id=step.id,
                status=ProgressStatusEnum.IN_PROGRESS,
            )

    async def reset_progress(self, user: User) -> None:
        first_step = await self.step_repo.get_first_active()
        if first_step:
            await self.user_repo.update(
                user,
                current_step_id=first_step.id,
                current_stage=first_step.stage,
                is_paused=False,
            )
