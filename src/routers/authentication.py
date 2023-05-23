from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.authentication.token import create_access_token
from src.database.database_connection import get_db
from src.database.hashing import Hash
from src.database.models import Users
from src.schemas.authentication import Token

router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model=Token)
def login(
    login_details: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> Token:
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

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
