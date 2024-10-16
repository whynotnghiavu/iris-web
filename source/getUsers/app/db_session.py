from contextlib import asynccontextmanager

from pathlib import Path

from environs import Env
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

env = Env()
file_env_path = Path(__file__).parent.parent.parent / ".env"
env.read_env(file_env_path)
logger.info(f"Loading environment from {file_env_path}")


db_user = env.str("POSTGRES_USER")
db_password = env.str("POSTGRES_PASSWORD")
db_url = env.str("POSTGRES_SERVER", default="db")
db_name = env.str("POSTGRES_DB")
logger.info(f"DB User: {db_user} and password: {db_password}")
SQLALCHEMY_DATABASE_URI = f"postgresql+asyncpg://{db_user}:{db_password}@{db_url}/{db_name}"
logger.info(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")


session = "placeholder"

async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URI,
    echo=False,
)

AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_db_session():
    async with AsyncSessionLocal() as session:
        logger.info("DB session created")
        try:
            yield session
        except Exception as e:
            logger.error(f"Error during DB session: {e}")
            await session.rollback()
            raise e
        finally:
            logger.info("Closing DB session")
            await session.close()


@asynccontextmanager
async def get_session():
    async with get_db_session() as session:
        yield session


async def get_db():
    async with get_session() as session:
        yield session
