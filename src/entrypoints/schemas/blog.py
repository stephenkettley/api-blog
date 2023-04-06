from pydantic import BaseModel


class Blog(BaseModel):
    """Structure of a blog to be created."""

    title: str
    body: str


class ShowAllBlogs(BaseModel):
    """Structure of all blogs being fetched."""

    id: int
    title: str

    class Config:
        """ORM config class."""

        orm_mode = True


class ShowOneBlog(BaseModel):
    """Strucutre of one blog being fetched."""

    title: str
    body: str

    class Config:
        """ORM config class."""

        orm_mode = True
