from sqlmodel import select

from loguru import logger
from typing import List

from app.db_session import get_db_session
from app.users.models.users import User

from fastapi import HTTPException


async def get_administrator_user() -> User:
    """
    Get administrator user

    Returns:
        User: Administrator user
    """
    try:
        logger.info("Getting administrator user")
        return await select_one_user("administrator")
    except Exception as e:
        logger.error(f"Error: {e}")
        return None


async def check_api_key(api_key: str, administrator_user: User):
    """
    Check API key

    Args:
        api_key (str): API key to check
        administrator_user (User): Administrator user

    Raises:
        HTTPException: If the API key is invalid
    """
    logger.info(f"Checking API key with api_key: {api_key}")

    if administrator_user.api_key != api_key:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )


async def select_all_users() -> List[User]:
    """
    Get all users

    Returns:
        List[User]: List of all users
    """
    logger.info(f"Get All Users Database IRIS")

    async with get_db_session() as session:
        statement = select(User)
        result = await session.execute(statement)
        users = result.scalars().all()
        return users


async def select_one_user(username: str) -> User:
    """
    Get one user

    Args:
        username (str): Username of the user to get

    Returns:
        User: User with the given username

    Raises:
        HTTPException: If the user with the given username not found
    """
    logger.info(f"Get One User with username: {username} Database IRIS")

    async with get_db_session() as session:
        statement = select(User).where(User.user == username)
        result = await session.execute(statement)
        user = result.scalars().first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail=f"User with username {username} not found"
            )

        return user
