import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base

# образец подключения базы данных sqlite3
# DB_LITE=sqlite+aiosqlite:///my_base.db   код из файла .env
# engine = create_async_engine(os.getenv('DB_LITE'), echo=True)

# BOT_TOKEN=7158259959:AAFgv0H3zVymsKexx87B0JPvixBG3zAu4S0
# DB_URL=postgresql+asyncpg://dev:golovchenko84@localhost:5432/bun_presentation
# ID_MAIN_ADMIN=1006569664
# ID_ADMINS=1006569664


engine = create_async_engine(os.getenv('DB_URL'), echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)