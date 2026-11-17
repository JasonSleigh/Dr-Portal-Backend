from sqlalchemy import Column, Integer, String, DateTime, Boolean, UUID as UUID_SQL
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base #! this needs to call the base from the database at production
from uuid import uuid4
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(UUID_SQL(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    public_key_pem = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime(timezone=True), nullable=False)
    updated_at = Column(DateTime, default=datetime(timezone=True), onupdate=datetime(timezone=True), nullable=False)
    deleted_at = Column(DateTime, nullable=True)