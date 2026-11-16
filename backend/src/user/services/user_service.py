from sqlalchemy.orm import Session
from backend.src.user.schemas.user_schemas import UserCreate, UserResponse
from backend.src.user.model.user_model import User, UUID_SQL
from uuid import uuid4
from datetime import datetime, timezone

def create_user(db: Session, user: UserCreate) -> UserResponse:
    db_user = User(
        email=user.email,
        password_hash=user.password_hash,
        role=user.role,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        public_key_pem=user.public_key_pem,
        is_active=True,
        is_verified=False,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc),
        deleted_at=None
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: UUID_SQL) -> UserResponse:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise ValueError("User not found")
    return db_user

def update_user(db: Session, user_id: UUID_SQL, user: UserCreate) -> UserResponse:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise ValueError("User not found")
    
    db_user.email = user.email
    db_user.password_hash = user.password_hash
    db_user.role = user.role
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.phone_number = user.phone_number
    db_user.public_key_pem = user.public_key_pem
    db_user.updated_at = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: UUID_SQL) -> None:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise ValueError("User not found")
    
    db_user.deleted_at = datetime.now(timezone.utc)
    db.commit()