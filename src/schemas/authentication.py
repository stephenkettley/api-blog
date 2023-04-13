from pydantic import BaseModel


class Login(BaseModel):
    """Structure for login details."""

    username: str
    password: str

    class Config:
        """ORM config class."""

        orm_mode = True


class Token(BaseModel):
    """Token info."""

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Token data."""

    email: str | None = None
