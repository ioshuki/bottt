from models.project_profile import ProjectProfile
from models.step import Step
from models.user import User
from schemas.llm_schema import EvaluationResult
from services.llm_service import LLMService
from services.project_service import ProjectService


class CoachService:
    def __init__(
        self,
        llm_service: LLMService,
        project_service: ProjectService,
    ) -> None:
        self.llm_service = llm_service
        self.project_service = project_service

    async def generate_daily_task_help(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> str:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.generate_daily_task_help(context)

    async def simplify_step(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> str:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.simplify_step(context)

    async def generate_example(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> str:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.generate_example(context)

    async def evaluate_user_response(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
        user_response: str,
    ) -> EvaluationResult:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.evaluate_user_response(context, user_response)

    async def summarize_project(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> str:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.summarize_user_project_state(context)

    async def generate_references(
        self,
        user: User,
        profile: ProjectProfile | None,
        step: Step | None,
    ) -> str:
        context = self.project_service.build_context(user, profile, step)
        return await self.llm_service.generate_references(context)
