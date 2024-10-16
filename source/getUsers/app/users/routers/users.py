from fastapi import APIRouter
from fastapi import Security
from loguru import logger
from typing import List

from app.users.utils.auth_handler import AuthHandler

from app.users.schema.users import UsersResponse
from app.users.services.universal import select_all_users
from app.users.services.universal import select_one_user


user_router = APIRouter(prefix="/api", tags=["users"])


@user_router.get(
    "/get-all-users",
    description="Get all users",
    response_model=List[UsersResponse],
    dependencies=[Security(AuthHandler().is_administrator())],
)
async def get_all_users() -> List[UsersResponse]:
    """
    Get all users

    Requires: Administrator role

    Returns:
        List of UsersResponse
    """
    logger.info(f"Request: Get All Users")
    return await select_all_users()


@user_router.get(
    "/get-one-user",
    description="Get One User",
    response_model=UsersResponse,
    dependencies=[Security(AuthHandler().is_administrator())],
)
async def get_one_user(
    username: str,
) -> UsersResponse:
    """
    Get one user

    Requires: Administrator role

    Args:
        username (str): Username of the user to get

    Returns:
        UsersResponse
    """
    logger.info(f"Request: Get One User")
    return await select_one_user(username)
