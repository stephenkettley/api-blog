from pydantic import BaseModel


class Login(BaseModel):
    """Structure for login details."""

    username: str
    password: str

    class Config:
        """ORM config class."""

        orm_mode = True
