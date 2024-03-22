from typing import AsyncIterable

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine

from fortuhost.applications.interfaces.uow import IUoW
from fortuhost.domain.dto.configs.db import DBConfig
from fortuhost.infrastructure.db.core import create_engine, create_session_factory
from fortuhost.infrastructure.db.uow import UoW


class DbProvider(Provider):
    scope = Scope.APP

    @provide
    async def get_engine(self, db_config: DBConfig) -> AsyncIterable[AsyncEngine]:
        engine = create_engine(db_config)
        yield engine
        await engine.dispose(True)

    @provide
    def get_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return create_session_factory(engine)

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            session_factory: async_sessionmaker[AsyncSession]
    ) -> AsyncSession:
        return session_factory()

    uow = provide(
        source=UoW,
        provides=IUoW,
        scope=Scope.REQUEST
    )
