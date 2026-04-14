from repositories.project_repository import ProjectRepository
from repositories.user_repository import UserRepository
from models.user import User
from models.project_profile import ProjectProfile


class OnboardingService:
    def __init__(
        self,
        user_repo: UserRepository,
        project_repo: ProjectRepository,
    ) -> None:
        self.user_repo = user_repo
        self.project_repo = project_repo

    async def get_or_create_user(
        self,
        telegram_id: int,
        username: str | None,
        name: str | None,
        language: str,
        timezone: str,
        daily_time: str,
        mode: str,
    ) -> tuple[User, bool]:
        user = await self.user_repo.get_by_telegram_id(telegram_id)
        if user:
            return user, False

        user = await self.user_repo.create(
            telegram_id=telegram_id,
            username=username,
            name=name,
            language=language,
            timezone=timezone,
            daily_time=daily_time,
            mode=mode,
        )
        await self.project_repo.create(user.id)
        return user, True

    async def get_profile(self, user_id: int) -> ProjectProfile | None:
        return await self.project_repo.get_by_user_id(user_id)

    async def update_profile(self, user_id: int, **kwargs) -> ProjectProfile:
        profile = await self.project_repo.get_by_user_id(user_id)
        if not profile:
            profile = await self.project_repo.create(user_id)
        return await self.project_repo.update(profile, **kwargs)

    async def complete_onboarding(
        self,
        user: User,
        project_name: str,
        goal: str,
        platforms: str,
    ) -> User:
        await self.project_repo.update(
            await self.project_repo.get_by_user_id(user.id),
            project_name=project_name,
            goal=goal,
            platforms=platforms,
        )
        return await self.user_repo.update(user, onboarding_completed=True)
