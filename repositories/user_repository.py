from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        result = await self.session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

    async def create(
        self,
        telegram_id: int,
        username: str | None,
        name: str | None,
        language: str,
        timezone: str,
        daily_time: str,
        mode: str,
    ) -> User:
        user = User(
            telegram_id=telegram_id,
            username=username,
            name=name,
            language=language,
            timezone=timezone,
            daily_time=daily_time,
            mode=mode,
        )
        self.session.add(user)
        await self.session.flush()
        return user

    async def update(self, user: User, **kwargs) -> User:
        for key, value in kwargs.items():
            setattr(user, key, value)
        await self.session.flush()
        return user

    async def list_active_users(self) -> list[User]:
        result = await self.session.execute(select(User))
        return list(result.scalars().all())
