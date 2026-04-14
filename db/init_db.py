from db.base import Base
from db.session import engine, SessionLocal
from db.seed_steps import seed_steps
import models  # noqa: F401


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        await seed_steps(session)
        await session.commit()
