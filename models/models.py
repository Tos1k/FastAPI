from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

Base = declarative_base()
metadata = MetaData()


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    permission = Column(JSON)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey(Role.id))
    registered_at = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
