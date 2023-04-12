from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.database_connection import get_db
from src.database.hashing import Hash
from src.database.models import Users
from src.schemas.authentication import Login
from src.schemas.user import UpdateUser

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=UpdateUser)
def login(login_details: Login, db: Session = Depends(get_db)) -> UpdateUser:
    """Validates and returns user logging in."""
    user = db.query(Users).filter(Users.email == login_details.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="username does not exist",
        )
    if not Hash.verify(user.password, login_details.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="incorrect password",
        )

    return user
