from pydantic import BaseModel


class Blog(BaseModel):
    """Structure of a blog creation request."""

    title: str
    body: str
    user_id: int


class ShowAllBlogs(BaseModel):
    """Structure of all blogs being fetched."""

    id: int
    title: str
    body: str

    class Config:
        """ORM config class."""

        orm_mode = True


class ShowOneBlog(BaseModel):
    """Structure of one blog being fetched."""

    title: str
    body: str

    class Config:
        """ORM config class."""

        orm_mode = True


class ShowTitles(BaseModel):
    """Structure of blogs when all users being shown."""

    title: str

    class Config:
        """ORM config class."""

        orm_mode = True
