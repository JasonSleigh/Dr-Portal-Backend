from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.src.user.services.user_service import create_user, get_user, update_user, delete_user
from backend.src.user.schemas.user_schemas import UserCreate, UserResponse
from backend.src.database import get_db
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    # FastAPI automatically validates user_id is a valid UUID!
    return get_user(db, user_id)

@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(
    user_id: UUID, 
    first_name: str | None = None, 
    last_name: str | None = None, 
    phone_number: str | None = None, 
    db: Session = Depends(get_db)
):
    return update_user(db, user_id, first_name=first_name, last_name=last_name, phone_number=phone_number)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return None