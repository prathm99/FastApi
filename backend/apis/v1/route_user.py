from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.session import get_db
from db.repository.user import create_new_user
from schemas.user import ShowUser

router = APIRouter()

@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    user = create_new_user(user=user, db=db)
    return user
