from pydantic import BaseModel


class User(BaseModel):
    """Structure of user creation request."""

    name: str
    email: str
    password: str


class ShowOneUser(BaseModel):
    """Structure of one user being fetched."""

    name: str
    email: str
    password: str

    class Config:
        """ORM config class."""

        orm_mode = True
