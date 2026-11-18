from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    # Accept plaintext password from client, NOT password_hash!
    password: str = Field(min_length=8, description="Plaintext password to be hashed on the backend")
    role: str = Field(..., description="e.g., 'doctor', 'specialist', 'practice_admin'")
    first_name: str
    last_name: str
    phone_number: str | None = None
    public_key_pem: str | None = None

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str
    first_name: str
    last_name: str
    phone_number: str | None = None
    public_key_pem: str | None = None
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None

    class Config:
        # Updated for Pydantic v2 (allows reading data directly from SQLAlchemy models)
        from_attributes = True