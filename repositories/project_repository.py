from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.project_profile import ProjectProfile


# ── standalone helpers (backward-compat) ──────────────────────────────────────

async def get_project_profile(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(ProjectProfile).where(ProjectProfile.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def create_project_profile(session: AsyncSession, user_id: int) -> ProjectProfile:
    profile = ProjectProfile(user_id=user_id)
    session.add(profile)
    await session.flush()
    return profile


async def update_project_profile(session: AsyncSession, profile: ProjectProfile, **kwargs) -> ProjectProfile:
    for key, value in kwargs.items():
        setattr(profile, key, value)
    await session.flush()
    return profile


# ── class wrapper (required by services/factory.py) ───────────────────────────

class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_user_id(self, user_id: int):
        return await get_project_profile(self.session, user_id)

    async def create(self, user_id: int) -> ProjectProfile:
        return await create_project_profile(self.session, user_id)

    async def update(self, profile: ProjectProfile, **kwargs) -> ProjectProfile:
        return await update_project_profile(self.session, profile, **kwargs)
