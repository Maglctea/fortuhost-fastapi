from collections.abc import AsyncGenerator
from uuid import uuid4

from asyncpg import Connection as BaseConnection
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from fortuhost.domain.dto.configs.db import DBConfig


class Connection(BaseConnection):
    def _get_unique_id(self, prefix: str) -> str:
        return f'__asyncpg_{prefix}_{uuid4()}__'


def create_engine(db_config: DBConfig) -> AsyncEngine:
    engine = create_async_engine(
        url=f'{db_config.full_url}?prepared_statement_cache_size=0',
        echo=True,
        echo_pool=db_config.echo,
        pool_size=10,
        connect_args={
            'statement_cache_size': 0,
            'connection_class': Connection,
        }
    )
    return engine


def create_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False
    )
    return session_factory


async def build_session(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
