from models.user import User
from repositories.user_repository import UserRepository


class SettingsService:
    def __init__(self, user_repo: UserRepository) -> None:
        self.user_repo = user_repo

    async def update_daily_time(self, user: User, daily_time: str) -> User:
        return await self.user_repo.update(user, daily_time=daily_time)

    async def update_timezone(self, user: User, timezone: str) -> User:
        return await self.user_repo.update(user, timezone=timezone)

    async def update_mode(self, user: User, mode: str) -> User:
        return await self.user_repo.update(user, mode=mode)

    async def pause(self, user: User) -> User:
        return await self.user_repo.update(user, is_paused=True)

    async def resume(self, user: User) -> User:
        return await self.user_repo.update(user, is_paused=False)
