from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.database_connection import get_db
from src.database.hashing import Hash
from src.database.models import Users
from src.schemas.user import ShowAllUsers, ShowOneUser, UpdateUser, User

router = APIRouter()


@router.post(
    "/user",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneUser,
    tags=["users"],
)
def create_new_user(user: User, db: Session = Depends(get_db)) -> ShowOneUser:
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


@router.get(
    "/user/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneUser,
    tags=["users"],
)
def get_unique_user(id: int, db: Session = Depends(get_db)) -> ShowOneUser:
    """Get one blog based on a unique id."""
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"user with id {id} does not exist",
        )
    return user


@router.put(
    "/user/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowOneUser,
    tags=["users"],
)
def update_unique_user(
    id: int,
    user: UpdateUser,
    db: Session = Depends(get_db),
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
        updated_blog = db.query(Users).filter(Users.id == id).first()

        return updated_blog


@router.get(
    "/user",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowAllUsers],
    tags=["users"],
)
def get_all_users(db: Session = Depends(get_db)) -> list[ShowAllUsers]:
    """Get all users from database."""
    users = db.query(Users).all()
    return users
