from sqlalchemy.orm import Session
from db.models.user import User
from schemas.user import UserCreate
from core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session) -> User:

    user = User(
        email=user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

