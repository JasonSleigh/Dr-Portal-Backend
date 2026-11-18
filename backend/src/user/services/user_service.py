from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from backend.src.user.schemas.user_schemas import UserCreate
from backend.src.user.model.user_model import User, UUID_SQL
from datetime import datetime, timezone
from passlib.context import CryptContext

# Set up Argon2 password context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate) -> User:
    # 1. Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # 2. Hash the plaintext password securely using Argon2
    secure_password_hash = hash_password(user.password)

    # 3. Create user record
    db_user = User(
        email=user.email,
        password_hash=secure_password_hash,
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

def get_user(db: Session, user_id: UUID_SQL) -> User:
    db_user = db.query(User).filter(User.id == user_id, User.deleted_at.is_(None)).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

def update_user(db: Session, user_id: UUID_SQL, first_name: str | None = None, last_name: str | None = None, phone_number: str | None = None) -> User:
    db_user = get_user(db, user_id) # Reuses the 404 check
    
    if first_name is not None:
        db_user.first_name = first_name
    if last_name is not None:
        db_user.last_name = last_name
    if phone_number is not None:
        db_user.phone_number = phone_number
        
    db_user.updated_at = datetime.now(timezone.utc)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: UUID_SQL) -> None:
    db_user = get_user(db, user_id) # Reuses the 404 check
    
    db_user.deleted_at = datetime.now(timezone.utc)
    db_user.is_active = False
    db.commit()