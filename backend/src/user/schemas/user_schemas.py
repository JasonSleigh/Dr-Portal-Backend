from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password_hash: str = Field(min_length=8)
    role: str
    first_name: str
    last_name: str
    phone_number: str
    public_key_pem: str

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    role: str
    first_name: str
    last_name: str
    phone_number: str
    public_key_pem: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True