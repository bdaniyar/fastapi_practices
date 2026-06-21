from asyncio import current_task
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, expire_on_commit=False, class_=AsyncSession
        )

    def get_scoped_session(self) -> async_scoped_session[AsyncSession]:
        return async_scoped_session(self.session_factory, scopefunc=current_task)

    async def session_dependency(self) -> AsyncGenerator[AsyncSession, None]:
        scoped_session = self.get_scoped_session()
        try:
            yield scoped_session()
        finally:
            await scoped_session.remove()


db_helper = DatabaseHelper(url=settings.db_url, echo=settings.db_echo)
