from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.database.database_connection import get_db
from src.repository.user import create, get_all, get_unique, update
from src.schemas.user import ShowAllUsers, ShowOneUser, UpdateUser, User

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ShowOneUser,
)
def create_new_user(user: User, db: Session = Depends(get_db)) -> ShowOneUser:
    """Creates a new user."""
    return create(
        user=user,
        db=db,
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ShowOneUser,
)
def get_unique_user(id: int, db: Session = Depends(get_db)) -> ShowOneUser:
    """Get one blog based on a unique id."""
    return get_unique(
        id=id,
        db=db,
    )


@router.put(
    "/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=ShowOneUser,
)
def update_unique_user(
    id: int,
    user: UpdateUser,
    db: Session = Depends(get_db),
) -> ShowOneUser:
    """Update a user with a unique id."""
    return update(id=id, user=user, db=db)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ShowAllUsers],
)
def get_all_users(db: Session = Depends(get_db)) -> list[ShowAllUsers]:
    """Get all users from database."""
    return get_all(db=db)
