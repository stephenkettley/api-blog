from pydantic import BaseModel

from src.schemas.blog import ShowOneBlog, ShowTitles


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


class UpdateUser(BaseModel):
    """Structure of update user request."""

    name: str
    email: str

    class Config:
        """ORM config class."""

        orm_mode = True


class ShowAllUsers(BaseModel):
    """Structure of all users being shown."""

    name: str
    email: str
    blogs: list[ShowTitles]

    class Config:
        """ORM config class."""

        orm_mode = True
