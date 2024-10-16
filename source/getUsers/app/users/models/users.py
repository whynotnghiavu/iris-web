import uuid
from flask_login import UserMixin
from sqlalchemy import Column
from sqlalchemy import BigInteger
from sqlalchemy import JSON
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.dialects.postgresql import UUID


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(UserMixin, Base):
    __tablename__ = 'user'

    id = Column(BigInteger, primary_key=True)
    user = Column(String(64), unique=True)
    name = Column(String(64), unique=False)
    email = Column(String(120), unique=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False,
                  server_default=text('gen_random_uuid()'), unique=True)
    password = Column(String(500))
    ctx_case = Column(Integer)
    ctx_human_case = Column(String(256))
    active = Column(Boolean())
    api_key = Column(Text(), unique=True)
    external_id = Column(Text, unique=True)
    in_dark_mode = Column(Boolean())
    has_mini_sidebar = Column(Boolean(), default=False)
    has_deletion_confirmation = Column(Boolean(), default=False)
    is_service_account = Column(Boolean(), default=False)
    mfa_secrets = Column(Text, nullable=True)
    webauthn_credentials = Column(JSON, nullable=True)
    mfa_setup_complete = Column(Boolean(), default=False)
