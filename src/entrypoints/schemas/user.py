from pydantic import BaseModel

from src.entrypoints.schemas.blog import ShowOneBlog


class User(BaseModel):
    """Structure of user creation request."""

    name: str
    email: str
    password: str


class ShowOneUser(BaseModel):
    """Structure of one user being fetched."""

    name: str
    email: str
    blogs: list[ShowOneBlog]

    class Config:
        """ORM config class."""

        orm_mode = True


class ShowCreator(BaseModel):
    """Structure of creator of a blog."""

    name: str

    class Config:
        """ORM config class."""

        orm_mode = True
