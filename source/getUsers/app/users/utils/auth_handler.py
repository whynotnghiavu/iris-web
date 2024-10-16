from fastapi import Depends
from fastapi.security import HTTPBearer


from app.users.services.universal import get_administrator_user
from app.users.services.universal import check_api_key


class AuthHandler:
    security = HTTPBearer(
        scheme_name='ADMINISTRATOR_API_KEY'
    )

    def is_administrator(self):
        async def _is_administrator(token: str = Depends(self.security)):
            api_key = token.credentials
            administrator_user = await get_administrator_user()
            await check_api_key(api_key, administrator_user)
            return administrator_user
        return _is_administrator
