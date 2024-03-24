import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from database.models import Base
from database.orm_query import orm_create_categories, orm_add_banner_description

from lexicon.lexicon_for_db import categories, description_for_info_pages

# образец подключения базы данных sqlite3
engine = create_async_engine(os.getenv('DB_LITE'), echo=True)

# DB_URL=postgresql+asyncpg://dev:golovchenko84@localhost:5432/bun_presentation
# engine = create_async_engine(os.getenv('DB_URL'), echo=True) # движок для постгрес

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_maker() as session:
        await orm_create_categories(session, categories)
        await orm_add_banner_description(session, description_for_info_pages)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)