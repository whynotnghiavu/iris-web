from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class UsersResponse(BaseModel):
    id: int
    user: str
    # name: str
    email: str
    # uuid: UUID
    # ctx_case: Optional[int] = None
    # ctx_human_case: Optional[str] = None
    # active: Optional[bool] = None
    api_key: Optional[str] = None
    # external_id: Optional[str] = None
    # in_dark_mode: Optional[bool] = None
    # has_mini_sidebar: Optional[bool] = None
    # has_deletion_confirmation: Optional[bool] = None
    # is_service_account: Optional[bool] = None
    # mfa_secrets: Optional[str] = None
    # webauthn_credentials: Optional[dict] = None
    # mfa_setup_complete: Optional[bool] = None

    class Config:
        orm_mode = True
