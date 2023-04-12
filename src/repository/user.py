from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.database.hashing import Hash
from src.database.models import Users
from src.schemas.user import ShowAllUsers, ShowOneUser, UpdateUser, User


def create(user: User, db: Session) -> ShowOneUser:
    """Creates a new user."""
    hashed_password = Hash.get_bcrypt_hashed_password(user.password)
    new_user = Users(
        name=user.name,
        email=user.email,
        password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_unique(id: int, db: Session) -> ShowOneUser:
    """Get one blog based on a unique id."""
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist",
        )
    return user


def update(
    id: int,
    user: UpdateUser,
    db: Session,
) -> ShowOneUser:
    """Update a user with a unique id."""
    fetched_user = db.query(Users).filter(Users.id == id)
    if not fetched_user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist for updating",
        )
    else:
        fetched_user.update({"name": user.name, "email": user.email})
        db.commit()
        updated_user = db.query(Users).filter(Users.id == id).first()

        return updated_user


def get_all(db: Session) -> list[ShowAllUsers]:
    """Get all users from database."""
    users = db.query(Users).all()
    return users
