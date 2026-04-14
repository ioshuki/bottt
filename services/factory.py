from sqlalchemy.ext.asyncio import AsyncSession

from repositories.user_repository import UserRepository
from repositories.project_repository import ProjectRepository
from repositories.step_repository import StepRepository
from repositories.progress_repository import ProgressRepository
from repositories.daily_plan_repository import DailyPlanRepository

from services.project_service import ProjectService
from services.onboarding_service import OnboardingService
from services.settings_service import SettingsService
from services.llm_service import LLMService
from services.coach_service import CoachService
from services.step_service import StepService
from services.planning_service import PlanningService


def build_services(session: AsyncSession) -> dict:
    user_repo = UserRepository(session)
    project_repo = ProjectRepository(session)
    step_repo = StepRepository(session)
    progress_repo = ProgressRepository(session)
    daily_plan_repo = DailyPlanRepository(session)

    project_service = ProjectService()
    onboarding_service = OnboardingService(user_repo, project_repo)
    settings_service = SettingsService(user_repo)
    llm_service = LLMService()
    coach_service = CoachService(llm_service, project_service)
    step_service = StepService(step_repo, progress_repo, user_repo, daily_plan_repo)
    planning_service = PlanningService(daily_plan_repo, step_repo)

    return {
        "user_repo": user_repo,
        "project_repo": project_repo,
        "step_repo": step_repo,
        "progress_repo": progress_repo,
        "daily_plan_repo": daily_plan_repo,
        "project_service": project_service,
        "onboarding_service": onboarding_service,
        "settings_service": settings_service,
        "llm_service": llm_service,
        "coach_service": coach_service,
        "step_service": step_service,
        "planning_service": planning_service,
    }
