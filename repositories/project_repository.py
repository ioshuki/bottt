from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.project_profile import ProjectProfile


class ProjectRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_user_id(self, user_id: int) -> ProjectProfile | None:
        result = await self.session.execute(
            select(ProjectProfile).where(ProjectProfile.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def create(self, user_id: int) -> ProjectProfile:
        profile = ProjectProfile(user_id=user_id)
        self.session.add(profile)
        await self.session.flush()
        return profile

    async def update(self, profile: ProjectProfile, **kwargs) -> ProjectProfile:
        for key, value in kwargs.items():
            setattr(profile, key, value)
        await self.session.flush()
        return profile
